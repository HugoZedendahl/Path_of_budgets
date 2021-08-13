import base64


class base64_functions:
    """base 64 encoding and decoding"""

    def encode_item_info(self, item_info):
        if (isinstance(item_info, str)):
            item_info_string_to_ascii = item_info.encode('ascii')
            base64_item_encoding = base64.b64encode(item_info_string_to_ascii)
            base64_item_output = base64_item_encoding.decode('ascii')
            return(base64_item_output)
        else:
            return("Invalid data")

    def decode_item_info(self, item_info):
        if (isinstance(item_info, str)):
            encoded_info_to_ascii = item_info.encode('ascii')
            base64_item_decoding = base64.b64decode(encoded_info_to_ascii)
            base64_item_decoded_output = base64_item_decoding.decode('ascii')
            return(base64_item_decoded_output)
        else:
            return("database error, type not valid")
