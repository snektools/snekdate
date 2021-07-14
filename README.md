# snekdate
snekdate is a small, simple date tool library we use for our dashboards. It is still a work in progress, we we're planning on adding multiple functions that make caching on a continuous datetime range for SQL queries simpler.

## SnekDate
All of the current functionality is in the `SnekDate` object. There are several static methods that can be used:

`SnekDate.now() # Returns the current date and time as a datetime objet`
<br>
`SnekDate.round_down_date(datetime, increment) # Returns a datetime object that is the result of rounding down to the increment specified`
<br>

The within function was removed from the package.

You can use the object to quickly return a date or a date range from the object in either a string or datetime format. The default value for the start date will be now if nothing is passed:

`SnekDate().start #Returns the value for now as a datetime object`

To create an offset, you can use the offset method. The start and end dates will automatically be determined.

`SnekDate().offset(day=1).start # returns the value a day into history from now
SnekDate().offset(day=1).end # returns the value of now
SnekDate().offset(day=1).range # Returns a tuple with the first index as the start date, the 2nd index as an end date`

There are properties that will return string values for each of these. Simply add "_str" to the property name:

`SnekDate().offset(day=1).start_str #Returns the string representation of the start date
SnekDate().offset(day=1).range_str #Returns a tuple of string representations of the start and end dates`