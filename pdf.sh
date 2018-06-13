absolute_path="$(cd "$(dirname "$1")"; pwd)/$(basename "$1")"
working_folder=$(dirname "${absolute_path}")
html_file=$(basename "${absolute_path}")

echo "$absolute_path"
echo "$working_folder"
echo "$html_file"


cmd="docker run -v $working_folder:/files openlabs/docker-wkhtmltopdf --print-media-type /files/$html_file /files/$2"
echo "$cmd"
eval $cmd