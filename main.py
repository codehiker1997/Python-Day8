# This is template for the message


msg_template = """
Hello {name},
This is Faizan Tanveer and having a request of fee concession from your collage
this is the best way to get approach to your {website},
Thank You,
{name2}

"""


# This is the function to format the msg present in python
def msg_format(name = "Google", website = "www.google.com", name2 = "Faizan Tanveer"):
    my_msg = msg_template.format(name = name, website = website, name2= name2)
    print(my_msg)


msg_format()

# This is the function to check what is the funciton of *args and **kwargs
def my_format(*args, **kwargs):
    print(args, kwargs)

my_format()


