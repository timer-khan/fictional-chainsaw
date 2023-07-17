'''
            self.__s = chain.upper() + "\n" + f"Skin: {name}\n"
            if chain == 'buff2tm':
                sell_price = round(sr * 0.95, 2)
                buy_price = self.get_buff_id_and_price(name)
                difference = round(sell_price / (buy_price['price'] * self.rubles_per_yuan), 3)
                self.__s += f"Buff price: {round(buy_price['price'] * self.rubles_per_yuan, 2)}\n" + \
                            f"TM SR price: {sell_price} ({sr})\n" + \
                            f"Difference: +{difference}"
            elif chain == 'tm2buff':
                sell_price = round(sr * 0.975, 2)
                buy_price = self.get_market_sell_price_and_market_item_id(name)
                difference = round(buy_price['price'] / sell_price, 3)
                self.__s += f"Buff SR price: {sell_price} ({sr})\n" + \
                            f"TM price: {buy_price['price']}\n" + \
                            f"Difference: -{difference}"
            print(self.__s)
            logger.debug("")
            if (chain == 'buff2tm' and difference >= (100 + self.__percentage) / 100) or (
                    chain == 'tm2buff' and difference <= (100 + self.__percentage) / 100):
                if chain == 'buff2tm':
                    buy = self.buff_buy(buy_price['skin_id'], buy_price['price'] * self.rubles_per_yuan)
                    buy_price = buy['price'] * self.rubles_per_yuan
                    self.__s += f'\n{buy["msg"]}'
                elif chain == 'tm2buff':
                    # buy = self.tm_buy(buy_price['skin_id'], buy_price['price'] * 100)
                    buy = True
                    buy_price = buy_price['price']
                if buy:
                    logger.success("BUY!!!")
                    self.__bot.send_message(self.__tg_id, self.__s)
                    buyed[name] = 1 if name not in buyed else buyed[name] + 1
                    with open(f"{chain}.csv", 'a', newline='', encoding='utf-8') as csvfile:
                        fieldnames = ['date', 'skin', 'buy_price', 'sell_price']
                        dictwriter_object = DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')
                        dictwriter_object.writerow({
                            "date": datetime.now().strftime("%d.%m.%Y"),
                            "skin": name,
                            "buy_price": round(buy_price, 2),
                            "sell_price": sell_price})
            '''
try:
    file = open('test.txt', 'r')
    input()
except KeyboardInterrupt:
    breakpoint()