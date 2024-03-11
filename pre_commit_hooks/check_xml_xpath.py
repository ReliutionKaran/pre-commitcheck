from lxml import etree
import sys

def check_xpath(filepath):
  """
  This function checks if a given XPath expression is valid against an XML file.

  Args:
      filepath: Path to the XML file.

  Returns:
      True if all XPaths are valid, False otherwise.
  """
  try:
    with open(filepath, 'rb') as f:
      xml_data = f.read()
  except IOError as e:
    print(f"Error opening file: {e}")
    return False

  try:
    # Parse the XML data
    tree = etree.fromstring(xml_data)
  except etree.XMLSyntaxError as e:
    print(f"Error parsing XML: {e}")
    return False

  # Get all potential XPath expressions from the command line arguments
  xpaths = sys.argv[2:]

  # Check each XPath expression
  for xpath in xpaths:
    try:
      # Use xpath on the parsed tree
      tree.xpath(xpath)
    except etree.XPATHSyntaxError as e:
      print(f"Invalid XPath expression: {xpath} - {e}")
      return False

  return True

if __name__ == "__main__":
  if len(sys.argv) < 3:
    print("Usage: python xpath_check.py <xml_file> <xpath1> [xpath2] ...")
    sys.exit(1)

  filepath = sys.argv[1]
  if not check_xpath(filepath):
    print("Failed XPath check. Please fix expressions and try again.")
    sys.exit(1)
  else:
    print("All XPaths are valid.")