#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <string.h>
#include <ctype.h>

void part1(long *sum, char *current_line, size_t len)
{
  char firstNumber = '\0';
  char lastNumber = '\0';

  for (int j = 0; j < len; j++)
  {
    const char current_char = current_line[j];

    if (isdigit(current_char))
    {
      if (firstNumber == '\0')
        firstNumber = current_char;
      lastNumber = current_char;
    }
  }

  long number = 0;
  number += firstNumber - '0';
  number *= 10;
  number += lastNumber - '0';

  *sum += number;
}

int main(int argc, char **argv)
{
  FILE *file;
  size_t len;
  size_t buffer_size = 0;
  char *current_line = NULL;
  unsigned int i;

  if (argc != 2)
  {
    fprintf(stderr, "Usage: %s file_name\n", argv[0]);
    return 1;
  }

  if ((file = fopen(argv[1], "r")) == NULL)
  {
    fprintf(stderr, "Could not open file: %s\n", argv[1]);
    perror("");
    return 1;
  }

  long sum1 = 0;

  for (int i = 1; (len = getline(&current_line, &buffer_size, file)) != -1; i++)
  {

    part1(&sum1, current_line, len);
    //TODO: part 2
  }

  printf("Day 1 Part 1: %ld\n", sum1);

  free(current_line);
  fclose(file);

  return 0;
}
