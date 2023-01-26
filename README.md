Welcome to my Wallapop Web Scraper.

This is a project which searches Wallapop periodically for listings of a given nature, as defined by the search url.

It then stores these listings in a PostgreSQL database. When it finds new listings, it sends a Telegram notification to let the user know that there are new listings which match the search criteria.

It also sends Telegram notifications to the user if the script encountered certain problems whilst running.