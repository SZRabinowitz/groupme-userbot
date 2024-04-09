from gmbotmodules.mymodules import logusage, sendMessage
import upsidedown, shlex, argparse

only_messages_with_text = True
moduleName = 'upsidedown'
helpString = '/upsidedown "<text>" will return the text upside down'
command = '/upsidedown'
case_sensitive = False


class CustomArgumentParser(argparse.ArgumentParser):
    msg_json = None
    def exit(self, status=0, message=None):
        if self.msg_json:
            sendMessage(message=self.msg_json, text=message)
            sendMessage(message=self.msg_json, text=self.format_help())
        # Call the parent class's error method
        super().exit(status=status, message=message)


def checkMessage(message):
    logusage()
    parser = CustomArgumentParser(prog=command)
    parser.msg_json = message
    parser.add_argument('text')
    args = parser.parse_args(shlex.split(message['text'])[1:])
    test = None
    if args.text:
        text = args.text
    sendMessage(message=message, text=upsidedown.transform(text))

