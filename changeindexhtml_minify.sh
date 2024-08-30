#!/bin/bash

change_html() {
    # Read HTML content
    html_content=$(cat ./public/index.html)

    # Perform replacements
    html_content=$(echo "$html_content" | sed -E 's/(class="flex flex-col h-screen px-[0-9]+ m-auto text-lg leading-7 max-w-7xl bg-neutral text-neutral-900 dark:bg-neutral-800 dark:text-neutral sm:px-[0-9]+ md:px-[0-9]+ lg:px-[0-9]+ scrollbar-thin scrollbar-track-neutral-200 scrollbar-thumb-neutral-400 dark:scrollbar-track-neutral-800 dark:scrollbar-thumb-neutral-600">)/\1\n/g' | sed -E 's/(px-|sm:px-|md:px-|lg:px-)[0-9]+/\10/g' | tr -d '\n')

    html_content=$(echo "$html_content" | sed 's/class="flex flex-col h-screen px-0 m-auto text-lg leading-7 max-w-7xl bg-neutral text-neutral-900 dark:bg-neutral-800 dark:text-neutral sm:px-0 md:px-0 lg:px-0 scrollbar-thin scrollbar-track-neutral-200 scrollbar-thumb-neutral-400 dark:scrollbar-track-neutral-800 dark:scrollbar-thumb-neutral-600">/class="flex flex-col h-screen px-0 m-auto text-lg leading-7 max-w-0xl bg-neutral text-neutral-900 dark:bg-neutral-800 dark:text-neutral sm:px-0 md:px-0 lg:px-0 scrollbar-thin scrollbar-track-neutral-200 scrollbar-thumb-neutral-400 dark:scrollbar-track-neutral-800 dark:scrollbar-thumb-neutral-600">/g')

    html_content=$(echo "$html_content" | sed -E 's/<div class=min-h-\[[0-9]+px\]><\/div>/<div class=min-h-[0px]><\/div>/g')

    html_content=$(echo "$html_content" | sed 's/<\/main><footer id=site-footer class="py-10 print:hidden">/<style>.stylecenter {text-align: center; margin-left: auto; margin-right: auto;}<\/style><\/main><footer id=site-footer class="py-10 print:hidden stylecenter">/g')

    html_content=$(echo "$html_content" | sed 's/<div class="mx-auto max-w-7xl p-0">/<style>.container {max-width: 64rem;}<\/style><div class="mx-auto container p-0">/g')

    # Write modified content back to the file
    echo "$html_content" > ./public/index.html

    echo "Replacement complete, modified HTML has been saved"
}

# Run the function every 1 second
while true; do
    change_html
    sleep 1
done