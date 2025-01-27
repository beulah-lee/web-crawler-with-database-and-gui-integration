#include "url_manager.h"
#include "utils.h"
#include <iostream>
#include <thread>
#include <mutex>
#include <vector>
#include <functional>
using namespace std;

void process_url(const string& url, const vector<string>& keywords, std::mutex& result_mutex) {
    string content = fetch_content(url);
    bool valid = is_content_valid(content, keywords);

    std::lock_guard<std::mutex> lock(result_mutex);
    if (valid) {
        cout << "Match Found: " << url << endl;
    } else {
        cout << "No Match: " << url << endl;
    }
}

void process_urls_multithreaded(const vector<string>& urls, const vector<string>& keywords) {
    std::mutex result_mutex;
    vector<thread> threads;

    for (const auto& url : urls) {
        threads.emplace_back([&]() {
            process_url(url, keywords, result_mutex);
        });
    }

    for (auto& thread : threads) {
        if (thread.joinable()) {
            thread.join();
        }
    }
}