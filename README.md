STLA Lite
=========

Lightweight timesheet system for State (or whomever) employees.

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg)](https://github.com/pydanny/cookiecutter-django/)
[![Known Vulnerabilities](https://snyk.io/test/github/401ode/stla-lite/badge.svg)](https://snyk.io/test/github/401ode/stla-lite)

**License:** MIT

# Goals

- An easy-to-use Timesheet entry system for employees, including the ability to allot hours spent on a project to a particular Grant Award and Grant Award Task/Service Area. 
- A back-end that makes it easy for managers to set up and maintain standard allocations, monitor employee hours, approve timesheets, etc. 
- Make a platform that is suited to the State of Rhode Island's needs, but easily adaptable to other states, municipalities, organizations, etc.


# High-Level Object Design

- Users / Employees:
	- Initial Import from Payroll System of:
		- Names
		- Job Titles
		- Classification
		- Eligible for Overtime
		- Employee ID Number
	- Generated / Gathered:
		- Usernames
		    - Ideally SSO to Office 365/Google Apps, but that's far off.
		- Supervisor (Hierarchical, gains supervisor-admin permissions)
		- Emergency Contact
		- Physical Working Location (Emergency Purposes)
		- Normal working hours (if applicable)
- Timesheets: 
	- Hours - Categorized:
		- Normal working
		- Exception: 
			- Vacation
			- Sick
			- Personal
			- Bereavement
			- Holiday (which we should know in advance) 
			- Jury Duty
			- Workers Compensation
			- Union Duties
			- Training, Conference, or Seminar
			- Other
	- For employees eligible for Overtime, calculation of overtime hours.
	- Approval by Supervisor
		- Timestamped
		- Upon approval, timesheet data eligible for export
		- Ideally, summary dashboard with employee timesheet data, exception hours, etc. 
	- Lookback:
	    - 90 day retrospective analysis of actual hours worked on a particular grant as a proportion of 100% of total worked hours, in order to properly allot exception hours to those grants proportionally. 
	    - Running average calculated at time of timesheet entry
- Allocations:
	- Grant Award - If an employee is doing work related to a Federal or other grant, the name/ID of the grant in question. 
	- Grant Award Task - The Grant Task (or Service Area) the employee was working on. 
- Pay Period: The two-week cycle in which employees are paid.
- Agency:
    - The Agency for whom the employee works.
    - The accounting system Agency Code corresponding to this Agency.
    - Cost Center:
        - Agencies have different "cost centers" across different divisions and functions. 
    - Additional fields necessary? Facilities list? 
- Reminders (via Mailgun):
	- Employees - Input your time.
	- Managers - Approve timesheets.
- Export Files for:
	- Payroll Systems (specifically old-school Mainframes)
	- ERPs (specifically Oracle E-Business Suite)

### Roadmap Features
- Request for Time Off
    - Subject to Supervisor Approval Process
- API: 
        - Establish a standard timesheet POST API for devices like timeclocks, punch-card systems, barcode readers, etc.


# Settings

Moved to [settings at Django Cookiecutter](http://cookiecutter-django.readthedocs.io/en/latest/settings.html). 


# Basic Commands

## Setting Up Your Users

- To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

- To create an **superuser account**, use this command:

    $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

## Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report::

    $ coverage run manage.py test
    $ coverage html
    $ open htmlcov/index.html

## Running tests with py.test

```

  $ py.test
```

## Live reloading and Sass CSS compilation

Moved to: [Live reloading and SASS compilation](http://cookiecutter-django.readthedocs.io/en/latest/live-reloading-and-sass-compilation.html)


# Sentry

Sentry is an error logging aggregator service. You can sign up for a free account at  https://sentry.io/signup/?code=cookiecutter  or download and host it yourself.
The system is setup with reasonable defaults, including 404 logging and integration with the WSGI application.

You must set the DSN url in production.


# Deployment

The following details how to deploy this application.


## Heroku

See detailed [cookiecutter-django Heroku documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-on-heroku.html).




