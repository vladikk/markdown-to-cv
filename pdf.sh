absolute_path="$(cd "$(dirname "$1")"; pwd)/$(basename "$1")"
working_folder=$(dirname "${absolute_path}")
html_file=$(basename "${absolute_path}")

absolute_path_output="$(cd "$(dirname "$2")"; pwd)/$(basename "$2")"
pdf_file=$(basename "${absolute_path_output}")

cmd="docker run -v $working_folder:/files openlabs/docker-wkhtmltopdf --print-media-type /files/$html_file /files/$pdf_file"
echo "$cmd"
eval $cmd