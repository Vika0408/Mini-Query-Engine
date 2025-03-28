import re

def convert_to_sql(nl_query):
    query_map = {
        "how many employees": "SELECT COUNT(*) FROM employees",
        "list all employees": "SELECT * FROM employees",
        "average salary": "SELECT AVG(salary) FROM employees"
    }
    
    for pattern, sql in query_map.items():
        if re.search(pattern, nl_query, re.IGNORECASE):
            return sql
    
    return None