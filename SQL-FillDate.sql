-- Deleting 

delete from dbo.Calc_Absensedays;
delete from dbo.Absense;
delete from dbo.Weather;

--Removing all Date_ID entries from weather data table
update dbo.WeatherData
set Date_ID = NULL;

delete from dbo.Date;


insert into dbo.Date(
	Day,
	Month_ID,
	Year, 
	DayOfWeek_ID,
	Format_1,
	Format_2
	)
select distinct
	DAY(Date) as Day, 
	MONTH(Date) as Month_ID,
	YEAR(Date) as Year,
	DATEPART(DW,Date)-1 as DayOfWeek_ID,
	CONVERT(Datetime, 
		CAST(YEAR(Date) AS nvarchar) + '-' + 
		CAST(MONTH(Date) AS nvarchar) + '-' + 
		CAST(DAY(Date) AS nvarchar) +
		' 06:50:00') as Format_1,

	CONVERT (Datetime,
		CAST(Year(Date) AS nvarchar) + '-' + 
		CAST(Month(Date) AS nvarchar) + '-' +
		CAST(Day(Date) AS nvarchar)) as Format_2
from dbo.AbsenseData;
 
update dbo.AbsenseData
	set Date_ID = dbo.Date.ID from dbo.Date
where dbo.AbsenseData.Date = dbo.Date.Format_2;

insert into dbo.Absense
(	
	State_ID,
	Date_ID
)
select 
	State as State_ID,
	Date_ID as Date_ID
from dbo.AbsenseData;

--Calculating the states per. day
insert into dbo.Calc_Absensedays
(
	Date_ID,
	State_Absent_Count,
	State_Present_Count
)

SELECT Date_ID, 
SUM(CASE WHEN State_ID =1 THEN 1 ELSE 0 END) AS State_Absent_Count, 
SUM(CASE WHEN State_ID =2 THEN 1 ELSE 0 END) AS State_Present_Count
FROM 
dbo.Absense
GROUP BY Date_ID;

update dbo.Calc_Absensedays
set Total_Student = State_Absent_Count + State_Present_Count;


--Setting ann Date_ID entries in weather data table
update dbo.WeatherData
set Date_ID = ID from dbo.Date
where dbo.Date.Format_1 = dbo.WeatherData.DateTime;


--Gets the entries from weatherdata that has a Date_ID and inputs them into weather table
Insert into dbo.Weather
(
	Date_ID,
	Temperature,
	Info
)
select
	Date_ID, 
	Temperature,
	Description as Info

from dbo.WeatherData
where dbo.WeatherData.Date_ID is not NULL;


-- Creating temporary table
with 
Weather_Month_Result as (
select dbo.Weather.Date_ID, dbo.Date.Month_ID, dbo.Weather.Temperature, dbo.Mid_Temperatur.Mid_Temp 
from dbo.Weather 
INNER JOIN dbo.Date ON dbo.Weather.Date_ID=dbo.Date.ID
INNER JOIN dbo.Mid_Temperatur ON dbo.Date.Month_ID=dbo.Mid_Temperatur.Month_ID)

--Setting the good_weather in weather table depending on the temporary table created
update dbo.Weather
set Good_Weather = 1
where (select Temperature from Weather_Month_Result where Weather_Month_Result.Date_ID = dbo.Weather.Date_ID) > (select Mid_Temp from Weather_Month_Result where Weather_Month_Result.Date_ID = dbo.Weather.Date_ID)
and dbo.Weather.Info = '';

--Setting all values that are null to value 0
update dbo.Weather
set Good_Weather = 0
where Good_Weather is NULL;
