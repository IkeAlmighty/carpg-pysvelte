# example api endpoint.
# I've made this pretty basic, (no regex or nested routes)
# and will likely regret it later.
# These are intended to just be simple GET request endpoints.

# to add another api endpoint simply
# create a new module in the api package
# and add a function called handle(): to it.
def handle():
  return 'hello!'