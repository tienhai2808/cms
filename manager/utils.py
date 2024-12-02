import pandas as pd

def is_manager(user):
  return user.is_superuser or user.groups.filter(name='Approver').exists()

def generate_date_range(start_date, end_date):
  date_range = pd.date_range(start=start_date, end=end_date)
  return [date.date() for date in date_range]