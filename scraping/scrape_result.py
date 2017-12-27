class ScrapeResult:
    def __init__(self, title, category, description, date, site_url, link_url, image_url):
        self.title = title
        self.category = category
        self.description = description
        self.date = date
        self.site_url = site_url
        self.url = link_url
        self.image_url = image_url

    def __str__(self):
        return f"{self.category}\n{self.title}\n{self.description}\n" \
               f"{self.date}\n{self.site_url}\n{self.url}\n{self.image_url}\n"

    def get_title(self):
        return self.title

    def get_category(self):
        return self.category

    def get_description(self):
        return self.description

    def get_date(self):
        return self.date

    def get_site_url(self):
        return self.site_url

    def get_url(self):
        return self.url

    def get_image_url(self):
        return self.image_url
