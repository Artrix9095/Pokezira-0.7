from flask import render_template as load
from flask import send_file as _getFile
from flask import request
import os
import sqlite3

class Forum(object):
  def __init__(self, bot):
      self.bot = bot

  @staticmethod
  def db(wanted):
    if wanted not in os.listdir('./'):
        raise FileNotFoundError
    c = sqlite3.connect(f"./{wanted}.db")
    return {'db': c, 'c': c.cursor()}


  def funcForum(self):
    @self.bot.route('/forum')
    def base():
        return load('forum.html')