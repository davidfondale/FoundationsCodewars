#Even or Odd

def odd_even(x):
    if x % 2 == 0:
        return "even";
    else:
        return "odd";

#Convert to String

def num_string(x):
    str = str(x);
    return str;

#Remove Spaces

def no_space(x):
    x_str = str(x);
    clean_x = x.strip();
    new_str = "";
    for char in clean_x:
        if char == " ":
            continue;
        new_str = new_str + char;
    return new_str;
