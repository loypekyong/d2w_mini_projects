// Transcrypt'ed from Python, 2022-09-15 10:32:17
var random = {};
import {AssertionError, AttributeError, BaseException, DeprecationWarning, Exception, IndexError, IterableError, KeyError, NotImplementedError, RuntimeWarning, StopIteration, UserWarning, ValueError, Warning, __JsIterator__, __PyIterator__, __Terminal__, __add__, __and__, __call__, __class__, __envir__, __eq__, __floordiv__, __ge__, __get__, __getcm__, __getitem__, __getslice__, __getsm__, __gt__, __i__, __iadd__, __iand__, __idiv__, __ijsmod__, __ilshift__, __imatmul__, __imod__, __imul__, __in__, __init__, __ior__, __ipow__, __irshift__, __isub__, __ixor__, __jsUsePyNext__, __jsmod__, __k__, __kwargtrans__, __le__, __lshift__, __lt__, __matmul__, __mergefields__, __mergekwargtrans__, __mod__, __mul__, __ne__, __neg__, __nest__, __or__, __pow__, __pragma__, __pyUseJsNext__, __rshift__, __setitem__, __setproperty__, __setslice__, __sort__, __specialattrib__, __sub__, __super__, __t__, __terminal__, __truediv__, __withblock__, __xor__, abs, all, any, assert, bool, bytearray, bytes, callable, chr, copy, deepcopy, delattr, dict, dir, divmod, enumerate, filter, float, getattr, hasattr, input, int, isinstance, issubclass, len, list, map, max, min, object, ord, pow, print, property, py_TypeError, py_iter, py_metatype, py_next, py_reversed, py_typeof, range, repr, round, set, setattr, sorted, str, sum, tuple, zip} from './org.transcrypt.__runtime__.js';
import * as __module_random__ from './random.js';
__nest__ (random, '', __module_random__);
var __name__ = '__main__';
export var gen_random_int = function (number, seed) {
	var ls = [];
	random.seed (seed);
	for (var i = 0; i < number; i++) {
		ls.append (i);
	}
	random.shuffle (ls);
	return ls;
	// pass;
};
export var generate = function () {
	var number = 10;
	var seed = 200;
	// pass;
	var array = gen_random_int (number, seed);
	// pass;
	var array_str = '';
	for (var i of array) {
		var i = str (i);
	}
	var array_str = ', '.join (array);
	var array_str = array_str + '.';
	document.getElementById ('generate').innerHTML = array_str;
};
export var insertationsort = function (array) {
	var n = len (array);
	for (var i = 1; i < n; i++) {
		var temp = array [i];
		while (i > 0) {
			if (temp < array [i - 1]) {
				array [i] = array [i - 1];
			}
			else {
				break;
			}
			i--;
		}
		array [i] = temp;
	}
};
export var sortnumber1 = function () {
	// pass;
	var array_str = document.getElementById ('generate').innerHTML;
	var array_str = array_str.__getslice__ (0, -(1), 1);
	var array = array_str.py_split (', ');
	insertationsort (array);
	for (var i of array) {
		var i = str (i);
	}
	var array_str = ', '.join (array);
	array_str += '.';
	document.getElementById ('sorted').innerHTML = array_str;
};
export var sortnumber2 = function () {
	var value = document.getElementsByName ('numbers') [0].value;
	if (value == '') {
		window.alert ('Your textbox is empty');
		return ;
	}
	var value = value.py_replace (' ', '');
	var array = list (value.py_split (','));
	for (var i = 0; i < len (array); i++) {
		try {
			array [i] = float (array [i]);
		}
		catch (__except0__) {
			if (isinstance (__except0__, ValueError)) {
				window.alert ('Invalid Symbols. Please key in numbers and seperate it by comma!');
				return ;
			}
			else {
				throw __except0__;
			}
		}
		if (array [i] != array [i]) {
			window.alert ('Invalid Symbols. Please key in numbers and seperate it by comma!');
			return ;
		}
	}
	var n = len (array);
	for (var outer_index = 1; outer_index < n; outer_index++) {
		var inner_index = outer_index;
		var temp = array [inner_index];
		while (inner_index > 0 && temp < array [inner_index - 1]) {
			array [inner_index] = array [inner_index - 1];
			var inner_index = inner_index - 1;
		}
		array [inner_index] = temp;
	}
	var array_str = '';
	for (var i = 0; i < n; i++) {
		array_str += array [i];
		if (i + 1 != n) {
			array_str += ',';
		}
	}
	document.getElementById ('sorted').innerHTML = array_str;
};

//# sourceMappingURL=library.map