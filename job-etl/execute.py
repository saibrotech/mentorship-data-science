# Import extract, transform and load
import extract, transform, load

# Ensure execute.py can only be run from bash
if __name__ == "__main__":
    # 1. Run Extract
    extract.main()
    # 2. Run Transform
    transform.main()
    #3. Run Load
    load.main()