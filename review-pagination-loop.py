# def generate_pagination(current, total):
#     pages = []

#     # Always show previous button
#     pages.append('<')

#     # Always show first page
#     pages.append('1')

#     # Left ellipsis
#     if current > 4:
#         pages.append('...')

#     # Pages around the current page
#     for i in range(current - 1, current + 2):
#         if i > 1 and i < total:
#             if i == current:
#                 pages.append(f'[{i}]')  # Highlight current
#             else:
#                 pages.append(str(i))

#     # Right ellipsis
#     if current < total - 3:
#         pages.append('...')

#     # Always show last page
#     if total > 1:
#         pages.append(str(total))

#     # Always show next button
#     pages.append('>')

#     return pages


# # Example usage
# pagination = generate_pagination(current=6, total=15)
# print(" ".join(pagination))


# def generate_pagination(current, total):
#     pages = []

#     # Previous button
#     pages.append('<')

#     # Always show first page
#     pages.append('1')

#     # Left ellipsis
#     if current >= 4:
#         pages.append('...')

#     # Pages around the current page
#     for i in range(current - 1, current + 2):
#         if 1 < i < total:
#             if i == current:
#                 pages.append(f'[{i}]')  # Highlight current page
#             else:
#                 pages.append(str(i))

#     # Right ellipsis
#     if current < total - 3:
#         pages.append('...')

#     # Always show last page
#     if total > 1:
#         pages.append(str(total))

#     # Next button
#     pages.append('>')

#     return pages


# # Taking user input
# try:
#     current_page = int(input("Enter current page: "))
#     total_pages = int(input("Enter total number of pages: "))

#     if current_page < 1 or current_page > total_pages:
#         print("Invalid input: Current page must be between 1 and total pages.")
#     else:
#         pagination = generate_pagination(current=current_page, total=total_pages)
#         print("Pagination Display:")
#         print(" ".join(pagination))

# except ValueError:
#     print("Please enter valid integer values.")

def generate_pagination(current, total):
    pages = []

    pages.append('<')  # Previous button

    if total <= 7:
        for i in range(1, total + 1):
            pages.append(f"[{i}]" if i == current else str(i))
    else:
        if current <= 4:
            for i in range(1, 5):
                pages.append(f"[{i}]" if i == current else str(i))
            pages.append("...")
            pages.append(str(total))
        elif current >= total - 3:
            pages.append("1")
            pages.append("...")
            for i in range(total - 3, total + 1):
                pages.append(f"[{i}]" if i == current else str(i))
        else:
            pages.append("1")
            pages.append("...")
            for i in range(current - 1, current + 2):
                pages.append(f"[{i}]" if i == current else str(i))
            pages.append("...")
            pages.append(str(total))

    pages.append('>')  # Next button
    return pages

# Input from user
try:
    current_page = int(input("Enter current page: "))
    total_pages = int(input("Enter total number of pages: "))

    if current_page < 1 or current_page > total_pages:
        print("Invalid input: Current page must be between 1 and total pages.")
    else:
        pagination = generate_pagination(current=current_page, total=total_pages)
        print("Pagination Display:")
        print(" ".join(pagination))

except ValueError:
    print("Please enter valid integer values.")
