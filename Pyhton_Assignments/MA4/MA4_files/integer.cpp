#include <cstdlib>
// Integer class
int _fib(int n);

class Integer {
public:
  Integer(int);
  int get();
  void set(int);
  int fib();

private:
  int val;
};

Integer::Integer(int n) { val = n; }

int Integer::get() { return val; }

void Integer::set(int n) { val = n; }
int Integer::fib() { return _fib(val); }

int _fib(int n) {
  if (n <= 1) {
    return n;
  }
  return _fib(n - 1) + _fib(n - 2);
}

extern "C" {
Integer *Integer_new(int n) { return new Integer(n); }
int Integer_get(Integer *integer) { return integer->get(); }
void Integer_set(Integer *integer, int n) { integer->set(n); }
int Integer_fib(Integer *integer) {
  if (!integer)
    return 0;
  return integer->fib();
}
void Integer_delete(Integer *integer) {
  if (integer) {
    delete integer;
    integer = nullptr;
  }
}
}