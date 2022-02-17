import tools.WebhookDestroyer.utilities.name as name
import tools.WebhookDestroyer.utilities.webhook as webhook
import tools.WebhookDestroyer.utilities.deleteWebhook as delhook

def start():
    name.main()
    webhook.main()
    delhook.main()