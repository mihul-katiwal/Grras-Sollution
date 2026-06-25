# dict
# d = {"name":"hello","age":20}

# print(d.keys())
# print(d.values())

# for i in d.keys():
#   print("key=",i)
#   print("value=",d[i])



# d = {
#   "Message": "Number of Post office(s) found: 6",
#   "Status": "Success",
#   "PostOffice": [
#     {
#       "Name": "Achrol",
#       "Description": "",
#       "BranchType": "Sub Post Office",
#       "DeliveryStatus": "Delivery",
#       "Taluk": "Jaipur",
#       "Circle": "Jaipur",
#       "District": "Jaipur",
#       "Division": "Jaipur Moffusil",
#       "Region": "Jaipur HQ",
#       "State": "Rajasthan",
#       "Country": "India"
#     },
#     {
#       "Name": "Jaitpura Khinchi",
#       "Description": "",
#       "BranchType": "Branch Post Office",
#       "DeliveryStatus": "Delivery",
#       "Taluk": "Jaipur",
#       "Circle": "Jaipur",
#       "District": "Jaipur",
#       "Division": "Jaipur Moffusil",
#       "Region": "Jaipur HQ",
#       "State": "Rajasthan",
#       "Country": "India"
#     },
#     {
#       "Name": "Kali Pahadi",
#       "Description": "",
#       "BranchType": "Branch Post Office",
#       "DeliveryStatus": "Delivery",
#       "Taluk": "Jaipur",
#       "Circle": "Jaipur",
#       "District": "Jaipur",
#       "Division": "Jaipur Moffusil",
#       "Region": "Jaipur HQ",
#       "State": "Rajasthan",
#       "Country": "India"
#     },
#     {
#       "Name": "Kant",
#       "Description": "",
#       "BranchType": "Branch Post Office",
#       "DeliveryStatus": "Delivery",
#       "Taluk": "Jaipur",
#       "Circle": "Jaipur",
#       "District": "Jaipur",
#       "Division": "Jaipur Moffusil",
#       "Region": "Jaipur HQ",
#       "State": "Rajasthan",
#       "Country": "India"
#     },
#     {
#       "Name": "Labana",
#       "Description": "",
#       "BranchType": "Branch Post Office",
#       "DeliveryStatus": "Delivery",
#       "Taluk": "Jaipur",
#       "Circle": "Jaipur",
#       "District": "Jaipur",
#       "Division": "Jaipur Moffusil",
#       "Region": "Jaipur HQ",
#       "State": "Rajasthan",
#       "Country": "India"
#     },
#     {
#       "Name": "Rajpurawas Tala",
#       "Description": "",
#       "BranchType": "Branch Post Office",
#       "DeliveryStatus": "Delivery",
#       "Taluk": "Jaipur",
#       "Circle": "Jaipur",
#       "District": "Jaipur",
#       "Division": "Jaipur Moffusil",
#       "Region": "Jaipur HQ",
#       "State": "Rajasthan",
#       "Country": "India"
#     }
#   ]
# }
# print(d["Message"])
# print(d["Status"])
# for i in d["PostOffice"]:
#   print(i["Name"])
#   print(i["Taluk"])
#   print(i["Circle"])
#   print(i["District"])
#   print(i["Division"])
#   print(i["Region"])
#   print(i["State"])
#   print(i["Country"])
#   print("\n")


# D = {"name":"hello","age":20}
# D.update({"name": "arya mains"})
# D['name'] = "arya mains new"
# print(D["age"])
# print(D)

# L = [20,30]
# print(L[0])


# D = {"name":"hello","age":20}
# D.update({"name": "arya mains"})
# D['name'] = "arya mains new"
# del D["name"]
# print(D)


# nested dict

# D = {"address":{"address1":{"city":"kukas city","district":"jaipur"},
#                 "address2":{"city":"gopalpura","district":"arya mains"}}}

# print(D["address"]["address1"]['city'])
# print(D["address"]["address1"]['district'])
# print(D["address"]["address2"]['city'])
# print(D["address"]["address2"]['district'])


# Example


data = {
  "catalogFeedType": "catalog_listing_page",
  "enable": False,
  "catalogs": [
    {
      "id": 2202811,
      "hero_pid": 11664045,
      "name": "Twinkling Fancy Bracelet & Bangles",
      "category_id": 1094,
      "sub_sub_category_name": "Bangles & Bracelets",
      "min_catalog_price": 220,
      "min_product_price": 220,
      "description": "Twinkling Fancy Bracelet & Bangles",
      "full_details": "Base Metal: Brass\nPlating: Gold Plated\nStone Type: Artificial Stones\nSizing: Non-Adjustable\nType: Bangle Set\nMultipack: 1\nSizes: 2.6\n\n\nDispatch: 1 Day",
      "share_text": "Catalog Name:Twinkling Fancy Bracelet & Bangles\nBase Metal: Brass\nPlating: Gold Plated\nStone Type: No Stone\nSizing: Non-Adjustable\nType: Bangle Style\nNet Quantity (N): Product Dependent\nSizes: 2.2, 2.4, 2.6, 2.8, 2.10\nDispatch: 2 Days\n\n*Proof of Safe Delivery! Click to know on Safety Standards of Delivery Partners- https://ltl.sh/y_nZrAV3",
      "hot": False,
      "type": "catalog",
      "pre_booking": False,
      "priority": 0,
      "num_suppliers": 0,
      "num_designs": 5,
      "image": "https://images.meesho.com/images/catalogs/2202811/cover/1/2/9240ae941b1dbcf0b22573a9abd42c429ec65981caac7a5b89321aa878380c314edd3382ac0866f54f5c10e3d3ca8de6041c92c7f70189be3be6082faa99b3a9_512.jpg",
      "collage_image": "https://images.meesho.com/images/catalogs/2202811/collages/1/1/9240ae941b1dbcf0b22573a9abd42c429ec65981caac7a5b89321aa878380c314edd3382ac0866f54f5c10e3d3ca8de6041c92c7f70189be3be6082faa99b3a9.jpg",
      "image_aspect_ratio": 1.77,
      "collage_image_aspect_ratio": 1.48,
      "created": "2020-11-05 18:11:12",
      "created_iso": "2020-11-05T18:11:12+0530",
      "valid": True,
      "trend": "",
      "popular": False,
      "has_mrp": True,
      "is_added_to_wishlist": False,
      "assured_details": {
        "is_assured": False,
        "message": "Best quality products from trusted suppliers."
      },
      "mall_verified": False,
      "story_images": [],
      "catalog_reviews_summary": {
        "rating_count_map": {
          "1": 458,
          "2": 358,
          "3": 695,
          "4": 1260,
          "5": 2858
        },
        "average_rating": 4,
        "absolute_average_rating": 5,
        "average_rating_str": "4.0",
        "rating_scale": 5,
        "review_count": 1568,
        "rating_count": 5629
      },
      "shipping": {
        "charges": 0,
        "discount": 0,
        "show_shipping_charges": False,
        "show_free_delivery": False,
        "is_express_delivery": False
      },
      "shipping_2": {
        "charges": 0,
        "discount": 0,
        "show_shipping_charges": False,
        "show_free_delivery": False,
        "is_express_delivery": False
      },
      "tags": [],
      "app_event_data": {
        "price_metadata": "eyJydG9DaGFyZ2UiOjAsImxvZ2lzdGljc0NoYXJnZSI6NDIuNzQsImNvZENoYXJnZSI6MTUuODEsImxvZ2lzdGljc0NoYXJnZURlbHRhQ29kIjowLCJsb2dpc3RpY3NDaGFyZ2VEZWx0YVBwZCI6MCwicnRvRGlzY291bnQiOjAsInNoaXBwaW5nQ2hhcmdlIjowLCJkZWxpdmVyeUZlZXMiOjAsInNoaXBwaW5nQ2hhcmdlc0FkanVzdG1lbnQiOjU3LCJ6b25hbERpc2NvdW50IjowLCJ6b25hbENoYXJnZSI6MCwic2VydmluZ1ByaWNlIjoyMjAsIm1heERpc2NvdW50UGVyY2VudGFnZSI6MCwicnRvUGVyY2VudGFnZUNvZCI6MC45NTg1MzYsInJ0b1BlcmNlbnRhZ2VQcGQiOjAuMDk3MjMyLCJpbnZlbnRvcnlDb3VudCI6NzIzLCJjb2REaXNjb3VudCI6MjQsImJmc0Rpc2NvdW50IjowLCJwZnNEaXNjb3VudCI6MCwic3VwcGxpZXJQcmljZSI6MTYzLCJ0YXhBcmJpdHJhZ2VXaXRob3V0R3N0IjotMC40MjI5LCJ0YXhBcmJpdHJhZ2VHc3QiOi0wLjAyMTYsInZhbG1vRGlzY291bnQiOi0xLjQxLCJpbnN0cnVtZW50YXRpb25PZmZlcnMiOnt9LCJydG9Ib2xkb3V0VHlwZSI6Im5vX3J0b19ob2xkb3V0Iiwic2VydmluZ1ByaWNlVHlwZSI6InByZW1pdW1fcmV0dXJuX3ByaWNlIiwiZGlmZmVyZW50aWFsUHJlcGFpZEFkanVzdG1lbnQiOjAsImRpZmZlcmVudGlhbFByZXBhaWRNYXJnaW4iOi01LjI0LCJwcmljZU1hcmdpbiI6MC45ODEyNjYsInBsYXRmb3JtUHJpY2VNYXJnaW5EZWx0YUNvZCI6LTYzLjYwNDM3LCJwbGF0Zm9ybVByaWNlTWFyZ2luRGVsdGFQcGQiOi0zMjguMDY0MTI3LCJmaXhlZEhhbmRsaW5nIjo5LjM3Njc4NCwiZm9yd2FyZFJhdGVDYXJkQ29kIjoyOS44MjkzNiwiZm9yd2FyZFJhdGVDYXJkUHBkIjoyOS44MjQ0MzQsInJldmVyc2VSYXRlQ2FyZENvZCI6MTcuNTcwMzU4LCJyZXZlcnNlUmF0ZUNhcmRQcGQiOjE4LjA5MjQ5LCJwbGF0Zm9ybVByaWNlGSTiOjAuMDMsInpvbmUiOiJEIiwiaXNNYWxsVmVyaWZpZWQiOmZhbHNlLCJpc1dhYXNTdXBwbGllciI6ZmFsc2UsInJldHVybkZhY3RvckNvZCI6MC4zMTI5NzcsInJldHVybkZhY3RvclBwZCI6MC4zODgyNzgsImNhc2hIYW5kbGluZ0NvZCI6My42NDU2ODQsImNhc2hIYW5kbGluZ1BwZCI6My43MDA0OTIsInN1cHBsaWVyUHJlcGFpZERpc2NvdW50IjozLCJkaWZmRGlzY291bnRpbmdEc0luc3RydW1lbnRhdGlvbkRhdGEiOnsicHJlcGFpZERpc2NvdW50QmVmb3JlIjoyNCwicHJlcGFpZERpc2NvdW50QWZ0ZXIiOjI0LCJwcm9kdWN0Q29ob3J0IjoiMyIsImNvZFNlcnZpbmdQcmljZSI6MjIwfSwicHJpbWFyeVByaWNlVHlwZSI6IiIsInNlY29uZGFyeVByaWNlVHlwZSI6IiIsInNzY2F0IjoiMTAwMTgiLCJucnRWcnNDb25maWciOiJjb25maWdfZCIsIndlaWdodCI6MTUwLCJ3ZWlnaHRTb3VyY2UiOiJESC1zb3J0ZXIgTS0wLTYgbW9udGhzIiwiYW92UHJpY2VNYXJnaW5GYWN0b3JDb2QiOjAuMDY3LCJhb3ZQcmljZU1hcmdpbkZhY3RvclBwZCI6MC4wNzgsInBsYXRmb3JtUHJpY2VNYXJnaW5UeXBlIjoiUEVSQ0VOVEFHRSIsImFiQ2FsbCI6InN1Y2Nlc3MiLCJwcmljZVBhdGgiOiJHZW5lcmFsOkxvZ2lzdGljc1YyIiwiZmluYWxQcmljZU1hcmdpbkNvZCI6MC4zNTcxMzgsImZpbmFsUHJpY2VNYXJnaW5QcGQiOi0yLjIzNzkxNiwiY29kUHJpY2UiOjIyMH0="
      },
      "gray_tags": [],
      "has_same_price_products": True,
      "product_images": [
        {"id": 11664045, "url": "https://images.meesho.com/images/products/11664045/481ab_512.jpg"},
        {"id": 11664043, "url": "https://images.meesho.com/images/products/11664043/bf54n_512.jpg"},
        {"id": 11664042, "url": "https://images.meesho.com/images/products/11664042/9bb46_512.jpg"},
        {"id": 11664044, "url": "https://images.meesho.com/images/products/11664044/27f69_512.jpg"},
        {"id": 11664046, "url": "https://images.meesho.com/images/products/11664046/4d32e_512.jpg"}
      ],
      "activated": "2020-11-05 23:07:13",
      "activated_iso": "2020-11-05T23:07:13+0530",
      "num_shares": "0 Shares",
      "margin": {"enabled": False},
      "price_type_id": "premium_return_price",
      "special_offers": {
        "display_text": "₹186 with 2 Special Offers",
        "offers": [
          {"type": "cod_unbundling", "amount": 24},
          {"type": "return_options", "amount": 10}
        ]
      },
      "consumer_share_text": "Hey, check out this product on Meesho! \r\n\r\nGet upto 25% OFF on your first order. Also grab extra 25% on new products every 3 hours!\r\n\nhttps://www.meesho.com/s/p/6y019?utm_source=s",
      "hero_product_name": "PLAIN GOLD PLATED BANGLE",
      "high_asp_enabled": False,
      "gst_type": "GSTIN",
      "state_code": "GJ",
      "affiliate_commission_text": "",
      "lc_commission_text": "10% Commission",
      "sale_marker": {"enabled": False},
      "combo_offer": {"enabled": False}
    },
    {
      "id": 116364416,
      "hero_pid": 397364085,
      "name": "New Trendy Earrings & Studs",
      "category_id": 1091,
      "sub_sub_category_name": "Earrings & Studs",
      "min_catalog_price": 174,
      "min_product_price": 174,
      "max_product_discount": 30,
      "total_discount_in_rs": 73,
      "discount_text": "₹73 off",
      "original_price": 247,
      "description": " Silver Real Silver Jewellery",
      "full_details": "Base Metal: Silver\nCertification: Seller Certification\nColor: Multicolor\nDimension L*B*H (Inch/mm/cm): 100\nNet Quantity (N): 1\nOccasion: Ethnic Party\nPlating: Oxidised Gold\nSilver Weight: 0.10 gm\nSizing: Non-Adjustable\nStone Type: Artificial Beads\nType: Earrings & Studs\nDispatch: 2-2 Days",
      "share_text": "Catalog Name:New Trendy Earrings & Studs\nBase Metal: Alloy\nPlating: Oxidised Gold\nSizing: Non-Adjustable\nStone Type: Artificial Beads\nType: Jhumkhas\nNet Quantity (N): 1\n\nDispatch: 1 Day\n\n*Proof of Safe Delivery! Click to know on Safety Standards of Delivery Partners- https://ltl.sh/y_nZrAV3",
      "hot": False,
      "type": "catalog",
      "pre_booking": False,
      "priority": 0,
      "num_suppliers": 0,
      "num_designs": 1,
      "image": "https://images.meesho.com/images/catalogs/116364416/cover/1/2/bf9ef8b9c5eaf1df0eb090fce9b251082d69b808fbb66c27b549a7ee4300930adf81aeb53527f86ca2fe009438c16f7dc934af19ddb9ec6cc80e2f9f41c601c2_512.jpg",
      "collage_image": "https://images.meesho.com/images/catalogs/116364416/collages/1/1/bf9ef8b9c5eaf1df0eb090fce9b251082d69b808fbb66c27b549a7ee4300930adf81aeb53527f86ca2fe009438c16f7dc934af19ddb9ec6cc80e2f9f41c601c2.jpg",
      "image_aspect_ratio": 1.77,
      "collage_image_aspect_ratio": 1.48,
      "created": "2024-03-15 15:58:34",
      "created_iso": "2024-03-15T15:58:34+0530",
      "valid": True,
      "trend": "",
      "popular": False,
      "has_mrp": True,
      "is_added_to_wishlist": False,
      "assured_details": {
        "is_assured": False,
        "message": "Best quality products from trusted suppliers."
      },
      "mall_verified": False,
      "story_images": [],
      "catalog_reviews_summary": {
        "rating_count_map": {
          "1": 67,
          "2": 39,
          "3": 75,
          "4": 94,
          "5": 314
        },
        "average_rating": 3.9,
        "absolute_average_rating": 4,
        "average_rating_str": "3.9",
        "rating_scale": 5,
        "review_count": 157,
        "rating_count": 589
      },
      "shipping": {
        "charges": 0,
        "discount": 0,
        "show_shipping_charges": False,
        "show_free_delivery": False,
        "is_express_delivery": False
      },
      "shipping_2": {
        "charges": 0,
        "discount": 0,
        "show_shipping_charges": False,
        "show_free_delivery": False,
        "is_express_delivery": False
      },
      "tags": [
        {"name": "NEXT DAY DISPATCH"}
      ],
      "app_event_data": {
        "price_metadata": "eyJydG9DaGFyZ2UiOjAsImxvZ2lzdGljc0NoYXJnZSI6NDAuOTUsImNvZENoYXJnZSI6MTYuMTksImxvZ2lzdGljc0NoYXJnZURlbHRhQ29kIjowLCJsb2dpc3RpY3NDaGFyZ2VEZWx0YVBwZCI6MCwicnRvRGlzY291bnQiOjAsInNoaXBwaW5nQ2hhcmdlIjowLCJkZWxpdmVyeUZlZXMiOjAsInNoaXBwaW5nQ2hhcmdlc0FkanVzdG1lbnQiOjU1LCJ6b25hbERpc2NvdW50IjowLCJ6b25hbENoYXJnZSI6MCwic3RyaWtlT2ZmUHJpY2UiOjI0Nywic2VydmluZ1ByaWNlIjoxNzQsIm1heERpc2NvdW50UGVyY2VudGFnZSI6MzAsInJ0b1BlcmNlbnRhZ2VDb2QiOjAuODE2MjU0LCJydG9QZXJjZW50YWdlUHBkIjowLjEwNjUwOSwiaW52ZW50b3J5Q291bnQiOjg5NzA4LCJjb2REaXNjb3VudCI6MjMsImJmc0Rpc2NvdW50IjowLCJwZnNEaXNjb3VudCI6MCwic3VwcGxpZXJQcmljZSI6MTY5LCJ0YXhBcmJpdHJhZ2VXaXRob3V0R3N0IjotMC4zOTYyLCJ0YXhBcmJpdHJhZ2VHc3QiOi0wLjAyMDMsInZhbG1vRGlzY291bnQiOi0xLjQxLCJpc0JycEJsb2NrZWQiOnRydWUsImluc3RydW1lbnRhdGlvbk9mZmVycyI6eyJzdXBwbGllck9mZmVycyI6W3siZGlzY291bnQiOjUwLCJvZmZlcklkIjoiMS1jeDZ4YVBBVXJWRmwxSzlXZTFqd1BhVXJlRFYyVVI2OWt1U3FZVkQ2MHhYIiwib2ZmZXJOYW1lIjoiRmxleGkgT2ZmZXIifV19LCJydG9Ib2xkb3V0VHlwZSI6Im5vX3J0b19ob2xkb3V0Iiwic2VydmluZ1ByaWNlVHlwZSI6InByZW1pdW1fcmV0dXJuX3ByaWNlIiwiZGlmZmVyZW50aWFsUHJlcGFpZEFkanVzdG1lbnQiOjAsImRpZmZlcmVudGlhbFByZXBhaWRNYXJnaW4iOi01LjI0LCJwcmljZU1hcmdpbiI6MC44MDUyNTQsInBsYXRmb3JtUHJpY2VNYXJnaW5EZWx0YUNvZCI6LTYzLjYwNDM3LCJwbGF0Zm9ybVByaWNlTWFyZ2luRGVsdGFQcGQiOi0zMjguMDY0MTI3LCJmaXhlZEhhbmRsaW5nIjo3Y29kU2VydmluZ1ByaWNlIjoxNzR9LCJwcmltYXJ5UHJpY2VUeXBlIjoiIiwic2Vjb25kYXJ5UHJpY2VUeXBlIjoiIiwic3NjYXIjOiIxMDEwOSIsIm5ydFZyc0NvbmZpZyI6ImNvbmZpZ19kIiwid2VpZ2h0IjoxNTAsIndlaWdodFNvdXJjZSI6IkRILXNvcnRlciBNLTAtNiBtb250aHMiLCJhb3ZQcmljZU1hcmdpbkZhY3RvckNvZCI6MC4wNjcsImFvdlByaWNlTWFyZ2luRmFjdG9yUHBkIjowLjA3OCwicGxhdGZvcm1QcmljZU1hcmdpblR5cGUiOiJQRVJDRU5UQUdFIiwiYWJDYWxsIjoic3VjY2VzcyIsInByaWNlUGF0aCI6IkdlbmVyYWw6TG9naXN0aWNzVjIiLCJmaW5hbFByaWNlTWFyZ2luQ29kIjowLjI5MzA3NywiZmluYWxQcmljZU1hcmdpblBwZCI6LTEuODM2NDk2LCJjb2RQcmljZSI6MTc0fQ=="
      },
      "gray_tags": [],
      "value_prop_tag": {"name": "NEXT DAY DISPATCH"},
      "has_same_price_products": True,
      "product_images": [
        {"id": 397364085, "url": "https://images.meesho.com/images/products/397364085/qlcit_512.jpg"}
      ],
      "activated": "2024-03-16 03:55:29",
      "activated_iso": "2024-03-16T03:55:29+0530",
      "num_shares": "0 Shares",
      "margin": {"enabled": False},
      "price_type_id": "premium_return_price",
      "special_offers": {
        "display_text": "₹151 with 1 Special Offer",
        "offers": [
          {"type": "cod_unbundling", "amount": 23}
        ]
      },
      "consumer_share_text": "Hey, check out this product on Meesho! \r\n\r\nGet upto 25% OFF on your first order. Also grab extra 25% on new products every 3 hours!\r\n\nhttps://www.meesho.com/s/p/6kkw39?utm_source=s",
      "hero_product_name": "Earrings Jhumkhi New Fancy Oxidize Small Jhumkhi Earrings For Women& Girls (Combo Of 12 Color) In Color Green, Red, Black, Pink, Maroon, White, Peach, Pista, Baby Pink, Grey, Aqua, Yellow",
      "high_asp_enabled": False,
      "gst_type": "GSTIN",
      "state_code": "GJ",
      "affiliate_commission_text": "",
      "lc_commission_text": "3% Commission",
      "sale_marker": {"enabled": False},
      "combo_offer": {"enabled": False}
    }
  ]
}

def print_values_recursive(item, current_path=""):
    """
    Recursively steps through dictionaries and lists to print every absolute value
    along with its dictionary key path or list index position.
    """
    if isinstance(item, dict):
        for key, value in item.items():
            new_path = f"{current_path}.{key}" if current_path else key
            print_values_recursive(value, new_path)
            
    elif isinstance(item, list):
        if not item:
            print(f"{current_path} -> []")
        for index, value in enumerate(item):
            new_path = f"{current_path}[{index}]"
            print_values_recursive(value, new_path)
            
    else:
        clean_value = str(item).replace('\n', ' \\n ')
        print(f"{current_path} -> {clean_value}")


print("--- STARTING VALUE EXTRACTION ---")
print_values_recursive(data)
print("--- EXTRACTION COMPLETE ---")