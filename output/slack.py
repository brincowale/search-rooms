from output.output import Output
from slackclient import SlackClient


class Slack(Output):
    def __init__(self, config):
        self.config = config
        self.slack = SlackClient(config['token'])

    def send_message(self, message):
        self.slack.api_call(
            "chat.postMessage",
            channel=self.config['channel'],
            text=message,
            username=self.config['username'],
            icon_emoji=self.config['icon_emoji']
        )
