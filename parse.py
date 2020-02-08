import feedparser
import json
import aiosqlite
import pprint



def parse_feeds():
    with open('feeds.json') as all_feeds_json:
        all_feeds = json.load(all_feeds_json)

    # json_feed_list = [link for link in all_feeds['politics']]
    f = feedparser.parse(all_feeds['politics'][0]['feed'])
    pprint.pp(f)
    # for i in range(len(all_feeds['politics'])):
    #     f = feedparser.parse(all_feeds['politics'][i]['feed'])
    #     print(all_feeds['politics'][i])

    

if __name__ == "__main__":
    parse_feeds()


# db = await aiosqlite.connect('marvin.db')
#         cursor = await db.cursor()
#         sql = ('UPDATE guilds SET ticket_channel = ? WHERE guild_id = ?')
#         val = ( str(ctx.channel.id), str(ctx.guild.id))
#         await cursor.execute(sql,val)
#         await db.commit()
#         await cursor.close()
#         await db.close()
