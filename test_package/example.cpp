#include <iostream>
#include <json11.hpp>

static std::string json_test = "{\n"
                        "  \"firstName\": \"John\",\n"
                        "  \"lastName\": \"Smith\",\n"
                        "  \"isAlive\": true,\n"
                        "  \"age\": 27,\n"
                        "  \"address\": {\n"
                        "    \"streetAddress\": \"21 2nd Street\",\n"
                        "    \"city\": \"New York\",\n"
                        "    \"state\": \"NY\",\n"
                        "    \"postalCode\": \"10021-3100\"\n"
                        "  },\n"
                        "  \"phoneNumbers\": [\n"
                        "    {\n"
                        "      \"type\": \"home\",\n"
                        "      \"number\": \"212 555-1234\"\n"
                        "    },\n"
                        "    {\n"
                        "      \"type\": \"office\",\n"
                        "      \"number\": \"646 555-4567\"\n"
                        "    },\n"
                        "    {\n"
                        "      \"type\": \"mobile\",\n"
                        "      \"number\": \"123 456-7890\"\n"
                        "    }\n"
                        "  ],\n"
                        "  \"children\": [],\n"
                        "  \"spouse\": null\n"
                        "}";

int main() {
  std::string err;
  json11::Json js = json11::Json::parse(json_test, err);
  if (err.empty() && js["address"]["city"].string_value() == "New York") {
    std::cout << "success" << std::endl;
    return EXIT_SUCCESS;
  }

  std::cout << "failure" << std::endl;
  return EXIT_FAILURE;
}
