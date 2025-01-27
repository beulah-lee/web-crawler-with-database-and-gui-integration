#ifndef UTILS_H
#define UTILS_H

#include <string>
#include <vector>

std::string fetch_content(const std::string& url);
bool is_content_valid(const std::string& content, const std::vector<std::string>& keywords);

#endif