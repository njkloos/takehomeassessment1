# This is a sample Python script.
import pandas as pd
import fuzzymatcher

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    a_with_geo = pd.merge(pd.read_csv("a__company.csv"),
                          pd.read_csv("a__geo.csv"),
                          on="geo_id",
                          how="outer"
                          )

    cb_address = pd.merge(pd.read_csv("b__company.csv"),
                          pd.read_csv("b__address.csv"),
                          on="b_entity_id",
                          how="outer")

    left_on = ["name","address1","country_x"]
    right_on = ["entity_name","location_street1","iso_country_x"]

    matched_results = fuzzymatcher.fuzzy_left_join(a_with_geo[["vendor_id","name","address1","country_x"]],
                                                   cb_address[["b_entity_id","entity_name","location_street1","iso_country_x"]],
                                                   left_on,
                                                   right_on,
                                                   left_id_col="vendor_id",
                                                   right_id_col="b_entity_id")

    matched_results[["vendor_id","b_entity_id"]].to_csv("matched_results.csv")

