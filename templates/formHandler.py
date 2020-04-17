# Import modules for CGI handling
import cgi, cgitb

# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields

print(form)

# first_name = form.getvalue('first_name')
# last_name = form.getvalue('last_name')
# print(first_name)
# print(last_name)