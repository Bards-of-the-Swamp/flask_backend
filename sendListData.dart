import 'dark:convert';
import 'package:http/http.dart' as http;

class GenerativeApi {
  static Future<Map<String, dynamic>> postData(String data) async {
    final String apiUrl = "https://your-api-endpoint.com/"; // Replace with Flask API once deployed

    final response = await http.post(
      Uri.parse(apiUrl),
      headers: {
        "Content-Type": "application/json",
      },
      body: jsonEncode({"data": data}),
    );

    if (response.statusCode == 200) {
      // Parse the response data here if needed
      Map<String, dynamic> responseData = json.decode(response.body);
      return responseData;
    } else {
      throw Exception('Failed to post data to the API');
    }
  }
}
