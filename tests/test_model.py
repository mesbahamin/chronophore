import collections
import filecmp
import json
import logging
import pathlib

from chronophore.model import Entry, Timesheet

logging.disable(logging.CRITICAL)

DATA_DIR = pathlib.Path(__file__).resolve().parent / 'data'
EXAMPLE_DATA = DATA_DIR.joinpath('data.json')
EXAMPLE_USERS = DATA_DIR.joinpath('users.json')


class TestTimesheet:

    with EXAMPLE_DATA.open() as f:
        example_sheet = json.load(f, object_pairs_hook=collections.OrderedDict)

    def test_getitem(self, timesheet):
        """Retrieve an entry from a Timesheet object
        using the index operator and the entry's uuid.
        """
        timesheet.sheet = self.example_sheet
        key = "2ed2be60-693a-44fe-adc1-2803a674ec9b"
        assert timesheet[key] == Entry(
            date="2016-02-17",
            name="Pippin Took",
            time_in="10:45",
            time_out=None,
            user_id="885894966"
        )

    def test_setitem(self, timesheet):
        """Assign an entry to a Timesheet object using
        the index operator.
        """
        e = Entry(
            date="2016-02-17",
            name="Frodo Baggins",
            time_in="10:45",
            time_out=None,
            user_id="889870966",
        )
        timesheet["test_key"] = e
        assert timesheet.sheet["test_key"] == e._asdict()

    def test_contains(self, timesheet):
        """Use membership operators to determine whether
        a Timesheet object has certain entries.
        """
        timesheet.sheet = self.example_sheet
        assert "2ed2be60-693a-44fe-adc1-2803a674ec9b" in timesheet
        assert "i don't exist" not in timesheet

    def test_len(self, timesheet):
        """Use len() to find out how many entries
        a Timesheet object has.
        """
        timesheet.sheet = self.example_sheet
        assert len(timesheet) == 3

    def test_find_signed_in(self, timesheet):
        """Find all entries of people that are currently signed in
        (all entries that have a time_in value, but not a time_out value).
        """
        timesheet.sheet = self.example_sheet
        timesheet._update_signed_in()
        expected_entries = ["2ed2be60-693a-44fe-adc1-2803a674ec9b"]
        assert timesheet.signed_in == expected_entries

    def test_add_signed_in(self, timesheet):
        """User signs in, and they are added to the list of currently
        signed in users.
        """
        key = "012345"
        e = Entry(
            date="2016-02-17",
            name="Frodo Baggins",
            time_in="10:45",
            time_out=None,
            user_id="889870966",
        )
        timesheet[key] = e
        assert key in timesheet.signed_in

    def test_remove_signed_in(self, timesheet):
        """User signs out, and they are removed from the list of currently
        signed in users.
        """
        timesheet.sheet = dict(self.example_sheet)
        key = "012345"
        e = Entry(
            date="2016-02-17",
            name="Frodo Baggins",
            time_in="10:45",
            time_out="13:30",
            user_id="889870966",
        )
        timesheet[key] = e
        assert key not in timesheet.signed_in

    def test_load_entry(self, timesheet):
        """Initialize an entry object with data from the timesheet."""
        timesheet.sheet = self.example_sheet
        entry = timesheet["1f4f10a4-b0c6-43bf-94f4-9ce6e3e204d2"]
        expected_entry = Entry(
            user_id="889870966",
            name="Merry Brandybuck",
            date="2016-02-17",
            time_in="10:45",
            time_out="13:30",
        )
        assert entry == expected_entry

    def test_save_entry(self, timesheet):
        """Add an entry to an empty timesheet."""
        key = "3b27d0f8-3801-4319-398f-ace18829d150"
        e = Entry(
            date="2016-02-17",
            name="Frodo Baggins",
            time_in="10:45",
            time_out="13:30",
            user_id="889870966",
        )
        timesheet[key] = e
        assert timesheet[key] == e

    def test_load_sheet(self, timesheet):
        """Load a sheet from a file."""
        with EXAMPLE_DATA.open() as f:
            timesheet.load_sheet(data=f)
        loaded_sheet = timesheet.sheet
        assert loaded_sheet == self.example_sheet

    def test_load_invalid_sheet(self, invalid_file):
        """Load an invalid json file. Make sure it gets
        renamed a with a '.bak' suffix.
        """
        backup = invalid_file.with_suffix('.bak')
        Timesheet(
            data_file=invalid_file,
            users_file=EXAMPLE_USERS
        )
        assert backup.is_file()
        assert not invalid_file.is_file()
        backup.unlink()

    def test_save_sheet(self, timesheet):
        """Save a sheet to a file."""
        timesheet.sheet = self.example_sheet
        timesheet.save_sheet()
        assert filecmp.cmp(str(timesheet.data_file), str(EXAMPLE_DATA))
