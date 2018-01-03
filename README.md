# Statcounter

Your convenient way to interact with Statcounter web analytics service
using Python

## Manual


### Installation

You can install this package from PyPi repository:
```
pip install statcounter
```

This package can run on Python 3 only (tested under Python 3.5 and
Python 3.6). Should also work on earlier Python 3 versions.
Python 2 is not supported and will not be supported in future
(However, PRs are welcome).

### Usage

First of all, you need to retrieve API password to use the Statcounter API.
Use [this](http://statcounter.com/api/password) link for that.
(**Note:** This is not the same as your user password!)


To start your work you need to initialize the Statcounter instance:
```python
from statcounter import Statcounter

statcounter = Statcounter('username', 'your-api-password')
```

#### Retrieve Statistics

Let consider an example of retrieving *summary* statistics.

This retrieves summary statistics for all period for project with `id=123`:
```python
stats = statcounter.summary(project_id=123)
print(stats)
```

You can get statistics for multiple projects:
```python
stats = statcounter.summary(project_id=[123, 456])
print(stats)
```

To view the last 50 rows (the default value for n is 20):
```python
stats = statcounter.summary(project_id=123, n=50)
print(stats)
```

Besides summary statistics, you are able to retrieve other types of
statistics supported by Statcounter service.
Available methods:

* `recent_visitors`
* `popular_pages`
* `entry_pages`
* `exit_pages`
* `came_from`
* `recent_came_from`
* `recent_keyword_activity`
* `search_engines`
* `recent_pageload_activity`
* `visit_length`
* `keyword_analysis`

For instance, this is the recent 50 visitors statistics with weekly date range:
```python
stats = statcounter.recent_visitors(
                DEMO_PROJECT_ID,
                DateRange.weekly(2017, 1, 2017, 2),
                n=50
            )
print(stats)
```

Please, use documentation in Docstrings for each method for details.
We also encourage to read the official Statcounter
[documentation](http://statcounter.com/api/docs/v3#retrieve-stats) about
statistics.

#### Date Range

You can retrieve stats using date range selection.
For instance, you want to retrieve stats from 1st week 2017 to 5th week 2017:

```python
from statcounter import DateRange

statcounter.summary(
        project_id=123,
        date_range=DateRange.weekly(2017, 1, 2017, 5)
    )
```

Available DateRange methods: `hourly`, `daily`, `weekly`, `monthly`, `quarterly`, `yearly`

#### Projects

You are able to (see the appropriate method in brackets):
* create new project in Statcounter (`create`)
* Increase log size for the project (`increase_log_size`)
* Retrieve details for all projects (`retrieve_projects_details`)
* Retrieve details for the selected project (`retrieve_selected_project_details`)

This is the example of creating a new project:
```python
statcounter.projects.create(
    website_title='Facebook',
    website_url='https://facebook.com'
)
```
For further details see docstrings and official Statcounter
(documentation)[http://statcounter.com/api/docs/v3#create-project].

#### Account details

There are two methods:
* `retrieve_log_size` - retrieve your current log size your payed plan
* `retrieve_user_details` - retrieve detailes about the user

Examples:
```python
statcounter.account.retrieve_log_size()
statcounter.account.retrieve_user_details()
```
