from discord.discord_hooks import Webhook


class SyncToDiscord:
    def __init__(self, url, color=3093151):
        self.url = url
        self.color = color

    def sync(self, unsynchronised_data):

        for item in unsynchronised_data:
            self.send_message(item)

    def send_message(self, item):
        embed = Webhook(self.url, color=self.color)
        embed.set_title(title=f"{item['title']} | {item['date']}", url=item['url'])
        embed.set_desc(item['description'])
        embed.set_image(item['image_url'])
        embed.set_footer(ts=True)
        embed.post()
