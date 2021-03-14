//g++ -std=c++2a -s -O1 solution_brute.cpp -o solution_brute -pthread
#include <ranges>
#include <algorithm>
#include <iostream>
#include <vector>
#include <thread>
int myrand(int &state)
{
    state = (state*1103515245 + 12345)&0x7fffffff;
    return (state>>16);
}
int main()
{
    int results[5];
    std::cout<<"Requires 5 values\n";
    std::ranges::for_each(results,[](int &n){std::cin>>n;});

    auto check=[&results](int state){
    if(std::ranges::all_of(results,[&state](int element){int rand=myrand(state); return rand==element;}))
    {
        std::cout<<myrand(state)<<std::endl;
        exit(EXIT_SUCCESS);
    }};

    int n=0;
    std::vector<std::thread> thr(8);
    for(int i=0;i<8;++i)
    {
        thr.at(i)=(std::thread(std::ranges::for_each,std::views::iota(n,0x10000000),check));
        n+=0x10000000;
    }
    for(auto &i:thr)
        i.join();
    return EXIT_FAILURE;
}
