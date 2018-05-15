#include <iostream>
#include <fstream>
#include <string>
#include <stdio.h>
#include <math.h>
#include <vector>
#include <queue>
#include <stdlib.h> 
using namespace std;


class Node
{
	public:
	int weight;
	int value;
	int level;
	double bound;
	double ratio;

	Node() {}

	Node(int weight_in, int value_in)
	{
		weight = weight_in;
		value = value_in;
		ratio = (double)value / (double)weight ;
	}
};


std::vector<Node> generate_Nodes(int amount) {
	std::vector<Node> nodes(amount);
	for (int i = 0; i < amount; i++) {
		Node node(rand() % 100 + 1, rand() % 100 + 1);
		nodes[i] = node;
	}
	return nodes;
}


void quicksort(std::vector<Node> *nodes, int start, int end) {
	double pivot = nodes->at((start + end) / 2).ratio;
	int x = start, y = end;
	while(x <= y)
	{
		while (nodes->at(x).ratio > pivot)
			x++;

		while (nodes->at(y).ratio < pivot)
			y--;

		if (x <= y) {
			Node tmp = nodes->at(x);
			nodes->at(x) = nodes->at(y);
			nodes->at(y) = tmp;
			x++;
			y--;
		}
	}
	if (start < y)
		quicksort(nodes, start, y);

	if (x < end)
		quicksort(nodes, x, end);
}


int bound(Node u, int size, int capacity, std::vector<Node> nodes)
{
	if (u.weight >= capacity)
		return 0;
	int val = u.value;
	int lvl = u.level + 1;
	int t_weight = u.weight;
	while ((lvl < size) && (t_weight + nodes.at(lvl).weight <= capacity))
	{
		t_weight += nodes.at(lvl).weight;
		val += nodes.at(lvl).value;
		lvl++;
	}
	if (lvl < size)
		val += (capacity - t_weight) * nodes.at(lvl).value / nodes.at(lvl).weight;
	return val;
}


int branch_and_bound(int capacity, std::vector<Node> nodes, int size) {
	int profit = 0;
	queue<Node> Q;
	Node u, v;
	u.level = -1;
	u.weight = 0;
	u.value = 0;
	Q.push(u);
	while (!Q.empty())
	{
		u = Q.front();
		Q.pop();

		if (u.level == size - 1)
			continue;

		v.level = u.level + 1;
		v.weight = u.weight + nodes.at(v.level).weight;
		v.value = u.value + nodes.at(v.level).value;

		if (v.weight <= capacity && v.value > profit)
			profit = v.value;
		v.bound = bound(v, size, capacity, nodes);
		if (v.bound > profit)
			Q.push(v);
		v.weight = u.weight;
		v.value = u.value;
		v.bound = bound(v, size, capacity, nodes);
		if (v.bound > profit)
			Q.push(v);
	}
	return profit;
}


int backtracking(int capacity, std::vector<Node> nodes, Node u, int profit) {
	if (u.level + 1 == nodes.size()) {
		if (u.weight <= capacity && u.value > profit)
			profit = u.value;
	}
	else {
		Node v = u;
		u.level++;
		u.weight = u.weight + nodes.at(u.level).weight;
		u.value = u.value + nodes.at(u.level).value;
		if(u.weight <= capacity && u.value > profit)
			profit = u.value;
		if (u.weight <= capacity)
			profit = backtracking(capacity, nodes, u, profit);
		u.value = v.value;
		u.weight = v.weight;
		if(u.weight <= capacity)
			profit = backtracking(capacity, nodes, u, profit);
	}
	return profit;
}


int generate_template(int size, string name) {
	unsigned int pow_set_size = pow(2, size);
	int counter, j;
	vector<int> tmp_array(size, 0);
	for (int i = 0; i < tmp_array.size(); i++) {
		tmp_array.at(i) = i+1;
	}

	ofstream myfile;
	myfile.open(name);
	for (counter = 0; counter < pow_set_size; counter++)
	{
		for (j = 0; j < size; j++)
		{
			if (counter & (1 << j))
				myfile << std::to_string(tmp_array.at(j)) + ", ";
			else
				myfile << "Nan, ";
		}
		myfile <<  "\n";
	}
	myfile.close();
	return 0;
}


double generate_and_test(int capacity, std::vector<Node> nodes) {
	std::vector<int> li;
	for (int x = 0; x < pow(2, nodes.size()); x++) {
		//std::vector<Node> xy;
		int flag = 1;
		double xy_weight_sum = 0;
		double xy_value_sum = 0;
		for (int y = 0; y < nodes.size(); y++) {
			if (x & (1 << y)) {
				if (xy_weight_sum + nodes.at(y).weight <= capacity) {
					 //xy.push_back(nodes.at(y));
					 xy_weight_sum += nodes.at(y).weight;
					 xy_value_sum += nodes.at(y).value;
				}
				else {
					flag = 0;
					break;
				}
			}
		}
		if (flag == 1) {
			li.push_back(xy_value_sum);
		}
	}
	auto it = max_element(std::begin(li), std::end(li));
	return *it;
}


int main()
{
	int capacity = 1000;
	int size = 5;
	string name = "example.csv";
	std::vector<Node> nodes = generate_Nodes(size);
	quicksort(&nodes, 0, size - 1);
	int profit = generate_and_test(capacity, nodes);
	//int profit_x = branch_and_bound(capacity, nodes, size);

	return 0;
}