import 'dart:convert';
import 'dart:io';

void main(List<String> arguments) {
  final line = stdin.readLineSync(encoding: utf8);
  final tokens = (line?.trim() as String).split(' ');
  final a = int.parse(tokens[0]);
  final b = int.parse(tokens[1]);

  print(a + b);
}
