from collections import defaultdict

class Find:

    def find_class(self, ObjectBs4, **kargs) -> dict:
        try:
            self.dict_ = defaultdict(str)
            img, name, price, cent = ObjectBs4.find(class_=kargs['img_element']), ObjectBs4.find(class_=kargs['name_element']), ObjectBs4.find(class_=kargs['price_element']), ObjectBs4.find(class_=kargs['cents_element'])
            
            self.dict_["img"] = img.attrs['src'] if img else ""
            print(img.attrs['src'])
            self.dict_["name"] = name.text if name else ""
            self.dict_["price"] = price.text + cent.text if price and cent else ""
        
            return dict(self.dict_)
        except Exception as e:
            print({"erro": True, "Motivo": "Erro ao realizar raspagem no site", "Log": {e}})