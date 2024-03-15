import json
import re

def is_single_file_contract(source_code):
    return (
        source_code.startswith("pragma") or
        source_code.startswith("//") or
        source_code.startswith("\r\n") or
        source_code.startswith("/*")
    )

def is_symbol_object(network):
    return "bsc" in network

def is_json_string(s):
    try:
        json.loads(s)
    except ValueError:
        return False
    return True

def parse_source_code_object(source_code, network):
    if is_symbol_object(network):
        double_curly_braces_pattern = r'^\{\{.*\}\}$'
        if re.match(double_curly_braces_pattern, source_code):
            source_code = source_code[1:-1]
            return json.loads(source_code)["sources"]
        return json.loads(source_code)
    elif is_json_string(source_code):
        return json.loads(source_code)
    return json.loads(source_code[1:-1])

def get_sources_object(parsed_source_code, network):
    if is_symbol_object(network):
        return parsed_source_code.items()
    if "sources" in parsed_source_code:
        return parsed_source_code["sources"].items()
    return parsed_source_code.items()

def get_contract_content_list(source_codes, network):
    contract_content = []
    if is_single_file_contract(source_codes["SourceCode"]):
        contract_content.append({
            "path": "contract.sol",
            "content": source_codes["SourceCode"]
        })
    else:
        parsed_source_code = parse_source_code_object(source_codes["SourceCode"], network)
        source_objects = [
            {"path": path, "content": content["content"]}
            for path, content in get_sources_object(parsed_source_code, network)
        ]
        contract_content.extend(source_objects)
    return contract_content


def cn(*classes):
    return " ".join(filter(None, classes))