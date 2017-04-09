/*
hdecode.cc
Ali Spittel
Lab 7 Huffman
12/12/14

This program decodes characters from an input file. It creates a tree from the
input file as specified. It then decodes for each letter based on the binary
values of each encoded character and the tree using 0 for left and 1 for right.
 It writes the decoded string to a file.
Note: Much of the code/ algorithmis from class.

*/

#include <cstdlib> 
#include <iostream>
#include <fstream>
#include <assert.h>

using namespace std;

struct h_node
{
  //this creates trees that have one piece of data per leaf
  char character;
  h_node * left;
  h_node * right;
  h_node(char c) : character(c), left(NULL), right(NULL){}
  h_node (h_node * left, h_node * right): left(left), right (right){}
};

string toBinary(int x)
{
  //turns a int into binary
  assert(x>=0);
  if (x==0)return "0";
  if (x==1)return "1";
  return toBinary(x/2)+toBinary(x%2);
}

string toBinary8(int x)
{
  //makes sure binary string is 8 chars long
  if (!(x >= 0) && !(x < 256)){
    cout<<x<<endl;
    exit(1);
  }
  
  string raw = toBinary(x+256);
  return raw.substr(1);
}

h_node * make_tree(ifstream & source)
{
  //takes the inputted "tree" and edits to an actual tree
  char key = source.get();
  assert(key=='L' or key == 'I');
  if (key =='L')
    return new h_node(source.get());
  if (key =='I'){ //recursion to keep making tree
    h_node * left = make_tree(source);
    h_node * right = make_tree(source);
    return new h_node(left, right);
  } 
  return NULL;
}

char tree_traverse(ifstream & source, h_node * tree, string & s)
{
  //Traverses the tree using binary code to find 
  //assert(s.length() >= 0);
  if (s.length() <= 1){ //adds to the binary if running out of working
                       //characters
    int next = source.get();
    s +=toBinary8(next);
  }
  if (tree->left == NULL && tree->right == NULL){
    return tree->character;
  }
  else {
    //recursion to move down the tree
    char q = s[0];
    s = s.substr(1);
    if(q =='1') 
      return tree_traverse(source, tree->right, s);
    if(q =='0') 
      return tree_traverse(source, tree->left, s);
  }
  return ' ';//will not happen
}

  
int main(int argc, char **argv){
 
  ifstream source(argv[1]);
 
  if (not source){
    // if the source file does not exist, quit the program
    cout<<"Cannot open "<<argv[1]<<" for reading."<<endl;
    exit(1);
  }
  //input the number of characters in the source file
  int num;
  source>>num;

  h_node * tree = make_tree(source); //create the tree

   string out1 = argv[1];
   out1 = out1.substr(0, out1.length()-4);//edit the output file
                                         //to not have the ".huf"
   ofstream out(out1.c_str());
   
   int start_char = source.get();
   string s = toBinary8(start_char); //start the function with this string

   for (int j = 0; j<num; j++)
     {  
       //decode all the characters and put them in the file
       char word = tree_traverse(source, tree, s);
       out.put(word);
     }
   remove(argv[1]);
   out.close();
}

