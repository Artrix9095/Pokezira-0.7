class trade:
  def init(bot):
    trade.bot = bot

    global self
    self = trade

    @self.bot.route('/test')
    def hm():
      return ':)'

