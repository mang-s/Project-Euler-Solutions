    #
    # Solved by mang-s
    # Date: 28/04/25
    #
    # https://projecteuler.net/problem=19
    # https://github.com/mang-s/Project-Euler-Solutions
    #

def count_sundays(start_year: int = 1900, start_day: str = "mon", end_year: int = 2001, target: str = "sun") -> int:
    
    days = ("mon", "tue", "wed", "thu", "fri", "sat", "sun")
    
    current_day_str = start_day
    sundays_counter = 0
    
    for year in range(start_year, end_year):
        
        months = {
        "jan": 31,
        "feb": 29 if is_leap_year(year) else 28,
        "mar": 31,
        "apr": 30,
        "may": 31,
        "jun": 30,
        "jul": 31,
        "aug": 31,
        "sep": 30,
        "oct": 31,
        "nov": 30,
        "dec": 31
    }
        
        for days_in_month in months.values():
            for current_day in range(0, days_in_month + 1):
                if current_day == 1 and current_day_str == target:
                    sundays_counter += 1
                    
                current_day_str = days[days.index(current_day_str) + 1] if current_day_str != "sun" else days[0]
            
    return sundays_counter

def is_leap_year(year: int) -> bool:
    return year % 4 == 0 and year % 400 != 0

if __name__ == "__main__":
    
    print(count_sundays())
    