from hoshino import Service, priv

sv = Service('yysy', manage_priv=priv.SUPERUSER, enable_on_default=True, visible=False)

@sv.on_fullmatch('有1说1')
async def yysy(bot, ev):
	await bot.finish(ev, '哪有1')