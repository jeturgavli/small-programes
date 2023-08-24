def create_advanced_search_query():
    keyword = input("Enter keyword: ")
    file_type = input("Enter file type (e.g., pdf): ")
    site = input("Enter site or domain to search within: ")
    intext = input("Enter keyword to search within page text: ")
    inurl = input("Enter keyword to search within URL: ")
    related = input("Enter related site or domain: ")
    exclude = input("Enter keyword to exclude: ")
    time_range_start = input("Enter start date for time range (YYYY-MM-DD): ")
    time_range_end = input("Enter end date for time range (YYYY-MM-DD): ")
    numeric_range_start = input("Enter start of numeric range: ")
    numeric_range_end = input("Enter end of numeric range: ")
    
    query = keyword
    
    if file_type:
        query += f" filetype:{file_type}"
    
    if site:
        query += f" site:{site}"
    
    if intext:
        query += f" intext:{intext}"
    
    if inurl:
        query += f" inurl:{inurl}"
    
    if related:
        query += f" related:{related}"
    
    if exclude:
        query += f" -{exclude}"
    
    if time_range_start and time_range_end:
        query += f" daterange:{time_range_start}..{time_range_end}"
    
    if numeric_range_start and numeric_range_end:
        query += f" {numeric_range_start}..{numeric_range_end}"
    
    return query

search_query = create_advanced_search_query()
print("Your advanced search query:", search_query)
