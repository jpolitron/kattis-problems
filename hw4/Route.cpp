#include "Route.hpp"
#include <string>
using namespace std;
Route::Route()
{
       	    stops[0] = "fooo st";
            stops[1] = "ayy st";
	    stops[2] = "kill breath";
	    stops[3] = "get her done";
	    stops[4] = "java st";

	current_position = 0;
}	
Route::Route(int current_position)
{
	this-> current_position = current_position;
	    stops[0] = "fooo st";
        stops[1] = "ayy st";
        stops[2] = "kill breath";
        stops[3] = "get her done";
        stops[4] = "java st";
}
string Route::getStop(int index)
{
	return stops[index];
}

