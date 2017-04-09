/*
randwrite.cc
Ali Spittel
Lab 5 Random Writing
11/7/14

This program takes various inputs from the user including a file containing
test. The program uses the usages of various combinations of letters to 
randomly generate a phrase, written to another file,
 of an inputted length starting with a "seed"
of length k which is also inputted. In essence, this program aims to 
write in a style similar to the author of the inputted work.

*/
#include <iostream>
#include <fstream>
#include <cstdlib>
#include <ctime>
#include "list.h"

using namespace std;




string new_seed(const list & char_list, int k)
{ 
  //creates the original seed
  size_t list_size = char_list.size();
  int rand_num = rand() % list_size;
  string seed;
  for(int i = 0; i< k; i++)
    //adds randomized letters in order from the list to the seed
    seed += char_list.get(rand_num + i); 
  return seed;   
}


list new_list(const list & char_list, string chars, size_t k)
{
  //creates new list of chars that follow the current seed
  //for each occurence of the seed
  list new_list;
  for(size_t i = 0; i<= char_list.size()-k; i++)
    {
      //variables declared in loop so they automatically reset
      string compare_string = ""; 
      size_t length = 0;
      for(size_t j = 0; j < k; j++)
	{
	  length = i + j; //edits later for use in comparison
	  compare_string += char_list.get(length);
	}
     
      if (compare_string == chars)
	  new_list.add(char_list.get(length + 1), new_list.size());
    }
    return new_list;    
}

char choose_random(const list & char_list)
{
  //chooses a char from a list of possible chars
  size_t list_size = char_list.size();
  int rand_num = rand() % list_size;
  char seed_add = char_list.get(rand_num);
  return seed_add;
}

//edits the seed back to length it was previously and adds the new  letter
void edit_seed(string & chars, char next, size_t k)
{
  //remove previous beginning of the seed
 chars = chars.substr(1,k);
 //add new end to seed
 chars+=next;
}


int main(int argc, char ** argv)
{
  //run the program!
  list allChars; //will hold all chars from text
  srand(time(NULL)); //re-randomizes the random function(from class)
  int k = atoi(argv[1]);//length of the seed (from project document)
  if (k<0){
    //makes sure k is non negative
    cout<<"K cannot be negative"<<endl;
    exit(1);
  }
  int length = atoi(argv[2]);//length of the writing 
  if (length < 0){
    //makes sure length is positive
    cout<<"Length cannot be negative"<<endl;
    exit(1);
  }
  if (length < k){ //makes sure length is higher than k
    cout<<"length cannot be shorter than k"<<endl;
    exit(1);
  }
  //partially from class
  //brings in file for the program to rea
  ifstream source(argv[3]);
  if (not source) {
     cout <<"Cannot open " <<argv[3] <<" for reading."<<endl;
     exit(1);
  }
  char ch; 
  while((ch=source.get()) != -1){
    //adds the characters from source into a list
    allChars.add(ch,allChars.size());
  }
  size_t size = allChars.size();
  int size1 = size;//since size() returns size_t, cast to int
  if(size1< k){ //make sure doc is longer than k
    cout<<"The file must be longer than k"<<endl;
    exit(1);
  } 
  ofstream result(argv[4]); //file that the program will write into
  if (not result){
    cout<<"Cannot open "<<argv[4]<<" for writing."<<endl;
    exit(1);
  }
  string _seed;
  char add_on;
  list _new_list;
  int length_check = 0; //used to stop loop
   while (length_check < length){
     // loop until meet length
    if (_new_list.size()!= 0){
      //checks to see if there is already a valid seed in place
      _new_list = new_list(allChars,_seed, k); //create a list from the seed
      add_on = choose_random(_new_list);//finds random letter to add to seed
      result.put(add_on);//outputs the new letter onto document (from C++ site)
      edit_seed(_seed, add_on, k);//edit the seed
      length_check ++;
    }
    else //if there is nothing following a seed in the text/ or there is no seed yet
      {
        if (length-length_check<=k){
	  //makes sure that adding the new seed won't overstep length
	  //if it does, makes a seed only the length until the end of document
	  _seed = new_seed(allChars,length-length_check);
	  result<<_seed;//output seed to result (from C++ site)
	  length_check += length-length_check;
	}

	else
	  //makes starting seed or new seed
	  {
	    _seed = new_seed(allChars,k);
	    result<<_seed;
	    length_check += k;
	  }
      }
   }
   source.close();
   result.close();  
}

