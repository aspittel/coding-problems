/*
hencode.cc
Ali Spittel
Lab 7 Huffman

This program encodes characters from an input file. It creates a tree from the
characters by combining nodes with the lowest character counts in the inputted
file. It then creates codes for each letter as to where they are on the tree,
using 0 for left and 1 for right. It writes a string to a .huf file that
shows the letters and what directions they are from the root. It also writes
the codes for each letter that the tree created.

*/

#include <cstdlib>
#include <iostream>
#include <fstream>

#include "priqueue.h"

using namespace std;

struct h_node
{
  //this creates trees that have two pieces of data stored in each leaf
  int ascii_val;
  int count;
  h_node * left;
  h_node * right;
  h_node(int a, size_t c) : ascii_val(a), count(c), left(NULL), right(NULL){}
  h_node (h_node * left, h_node * right):count(left -> count + right -> count),
					 left(left), right (right){}
};

int count [256]; // number of each character in the file
string codes [256]; //keeps track of all the written codes
size_t length = 0; //length of the file


int priority_fn(h_node * const & tree)
{
  // This is the priority function for the priqueue file
  // It is the size of the given tree
  return tree -> count;
}

void prepend_all(h_node * tree, char c)
{
  //Adds a 0 to all left character's leaves code and 1
  //to right character's leaves code recursively
  if (tree->left == NULL)
    codes[tree->ascii_val]=c+codes[tree->ascii_val];
  else {
    prepend_all(tree->left, c);
    prepend_all(tree->right, c);
  }
}

void write_tree(h_node * tree, ofstream & out)
{
  // writes a tree to the output file using L to demarcate a leaf and
  // I for each branch
  if (tree->left == NULL)
    out<<"L"<<(char)tree->ascii_val;
  else
    {
      out<<"I";
      write_tree(tree->left, out);
      write_tree(tree->right, out);
    }
}

int fromBinary (string s)
{
  //function that converts binary string to int
  assert(s.size()>0 && '0'<=s[0] && s[0]<= '1');
  if(s=="0") return 0;
  if(s=="1") return 1;
  return 2* fromBinary(s.substr(0, s.size()-1))+s[s.size()-1]-'0';
}

int main (int argc, char ** argv)
{
  for (size_t i = 0; i < 256; i++)
    //sets all values initially to 0
    count [i] = 0;

  ifstream source(argv[1]);
  if (not source){
    // if the source file does not exist, quit the program
    cout<<"Cannot open "<<argv[1]<<" for reading."<<endl;
    exit(1);
  }

  int i;
  while(i != -1){
    // increases the counter for the number of occurances of a letter
    i = source.get();
    if (i == -1) break;
    count[i]++;
    length++;
  }

  priqueue <h_node *> q(priority_fn);

  for (size_t j = 0; j < 256; j++)
    if(count[j]>0)
      //add any letters to the tree that are in the phrase
      q.add(new h_node(j, count[j]));

  while(q.size() != 1){
    //combine trees and edit binary values for characters
    h_node * left = q.front();
    q.remove_front();
    h_node * right = q.front();
    q.remove_front();
    q.add(new h_node(left, right));
    prepend_all(left, '0');
    prepend_all(right, '1');
  }

  //create a file to write code into;
  string huf_file = argv[1];
  huf_file += ".huf";
  ofstream out(huf_file.c_str()); //since ofstream does not take string
                                  //make int c string (Used C++ site)

  out<<length; //write the phrase length to the file
  write_tree(q.front(),out); //add the tree to the file

  source.close(); //close source to restart reading of file
  ifstream source1(argv[1]);

  int k;
  string s;
  while(k != -1){
    //add encoded letters to file
    while (s.length()<8){
      k = source1.get(); //make string 8 chars long][[
      if (k == -1) break; //make sure still not empty
      s += codes[k];
    }
    if(s.size()<8) break;  //pad the string
    int encoded_char = fromBinary(s.substr(0,8));
    out.put(encoded_char);
    s = s.substr(8);
  }

  while(s.size()%8 != 0)
    //"pad" the superstring with 0's
    s += '0';

  int encoded_char = fromBinary(s);//add final encoded char to file
  out.put(encoded_char);

  out.close();  //close output file
  remove(argv[1]);  //delete original file
}
