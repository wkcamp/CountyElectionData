# Commit History
If you wish to view all commits made to this project, [you can find them here](https://github.com/wkcamp/CountyElectionData/commits/master "you can find them here").
# Directory Descriptions
## archived/
contains unsuccessful Python scripts that used Python PDF libraries like Pandas to process county PDFs.
## breakdown_scripts/
contains a generic script, `generic_breakdown.py`, to process county PDFs based on text output, which looks like:

> 01 Ash 1A  
> Polling  
> Absentee  
> Provisional  
> Total  
> 02 Ash 1B  
> Polling  
> Absentee  
> Provisional  
> Total  
> etc...  

contains a county-specific script, `instanced_version_generic.py`, that demonstrates the method of processing the aforementioned text output.

## Categorization_scripts/
contains a script, `create_categories.py`, that creates a directory structure for county categorizations. You can view an example of the structure in this file.

## Excel_sheets/
Contains three excel sheets that provide explicitly the categories and subcategories of each county and the pages of targeted referenda.

## Output/
Contains a JSON output folder to demonstrate  how one can create nested data structures to contain all the county PDF data. Because the breakdown scripts break votes down based on sections (which are pages for now), the JSON data follows the following output:
```json
{
	PRECINCT:
		[ 
			[Section Number 1, Yes Vote, No Vote],
			[Section Number 2, Yes Vote, No Vote],
			etc...
		]
}
```

Contains `PDF_raw_text` which is the text output from each county PDF, obtained via the library called [textract.](https://textract.readthedocs.io/en/stable/ "textract.")

### requirements.txt
Contains the necessary dependencies to run these scripts.

To install them:
1. Check that your computer has the Python package manager [pip](https://pip.pypa.io/en/stable/ "pip") installed, using this command in your terminal
` $ pip --version`
2. Install [virtualenv](https://docs.python-guide.org/dev/virtualenvs/ "virtualenv") which will locally (in the project's diectory rather than on your entire computer) install the package requirements.
`pip install virtualenv`
3. Create a virtual environment for this project.
```
	$ cd my_project_folder
	$ virtualenv your_virtual_env_name
```
I use `venv` for mine.

4. Within this project folder, activate the virtual environment
`$ source venv/bin/activate`, which gives you something like `(venv) $ ...` in your terminal.  

5. Install the project requirements in your terminal.
`$ pip install -r requirements.txt`

If you have any issues, please read the links provided or contact me.