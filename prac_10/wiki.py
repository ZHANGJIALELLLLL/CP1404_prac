import wikipedia


def search_wikipedia():
    """Search Wikipedia for pages and display their details."""
    print("Wikipedia Search Program")
    print("Enter a page title or search phrase (blank to quit)")

    should_continue = True

    while should_continue:
        search_term = input("\nEnter page title: ").strip()
        if not search_term:
            print("Thank you.")
            should_continue = False
            continue

        try:
            # First try to get suggestions if the exact page isn't found
            suggestions = wikipedia.search(search_term)

            # Try to get the page with autosuggest disabled for more accurate results
            page = wikipedia.page(search_term, auto_suggest=False)

            # If successful, print the page details
            print("\n" + page.title)
            print(page.summary)
            print(page.url)

        except wikipedia.exceptions.DisambiguationError as e:
            # Handle cases where the term is ambiguous
            print(f"We need a more specific title. Try one of the following, or a new search:")
            print(e.options[:10])  # Show first 10 options to avoid overwhelming output

        except wikipedia.exceptions.PageError:
            # Handle cases where the page doesn't exist
            print(f'Page id "{search_term}" does not match any pages. Try another id!')

        except Exception as e:
            # Handle any other unexpected errors
            print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    search_wikipedia()