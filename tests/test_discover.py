import os
import core.discover as discover

def test_discover_main_creates_csv(tmp_path):
    # Override the output file path
    test_file = tmp_path / "products.csv"
    original_output = discover.OUTPUT_FILE
    discover.OUTPUT_FILE = str(test_file)

    # Run the discovery logic
    discover.main()

    # Check that the file was created and is not empty
    assert test_file.exists()
    assert test_file.stat().st_size > 0

    # Restore original path
    discover.OUTPUT_FILE = original_output

