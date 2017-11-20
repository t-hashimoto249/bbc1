#include <stdio.h>
#include <stdlib.h>
#include <memory.h>
#include <time.h>

u_int32_t parse_u_int8_t(u_int8_t* binary, u_int8_t* header){
    u_int32_t length = 0;

    memcpy(header, binary, sizeof(u_int8_t));
    binary = binary + sizeof(u_int8_t);
    length = length + sizeof(u_int8_t);

    return length;
}

typedef struct {
    u_int8_t value;
    struct List_u_int8_t* next;
} List_u_int8_t;

u_int32_t parse_list_u_int8_t(u_int8_t* binary, List_u_int8_t* header){
    u_int32_t length = 0;

    length = parse_u_int8_t(binary, &(header->value));
    binary = binary + sizeof(u_int8_t);

    return length;
}

u_int32_t parse_u_int16_t(u_int8_t* binary, u_int16_t* header){
    u_int32_t length = 0;

    memcpy(header, binary, sizeof(u_int16_t));
    *header = ntohs(*header);
    binary = binary + sizeof(u_int16_t);
    length = length + sizeof(u_int16_t);

    return length;
}

typedef struct {
    u_int16_t value;
    struct List_u_int16_t* next;
} List_u_int16_t;

u_int32_t parse_list_u_int16_t(u_int8_t* binary, List_u_int16_t* header){
    u_int32_t length = 0;

    length = parse_u_int16_t(binary, &(header->value));
    binary = binary + sizeof(u_int16_t);

    return length;
}

u_int32_t parse_u_int32_t(u_int8_t* binary, u_int32_t* header){
    u_int32_t length = 0;

    memcpy(header, binary, sizeof(u_int32_t));
    *header = ntohl(*header);
    binary = binary + sizeof(u_int32_t);
    length = length + sizeof(u_int32_t);

    return length;
}

typedef struct {
    u_int32_t value;
    struct List_u_int32_t* next;
} List_u_int32_t;

u_int32_t parse_list_u_int32_t(u_int8_t* binary, List_u_int32_t* header){
    u_int32_t length = 0;

    length = parse_u_int32_t(binary, &(header->value));
    binary = binary + sizeof(u_int32_t);

    return length;
}

u_int32_t parse_u_int64_t(u_int8_t* binary, u_int64_t* header){
    u_int32_t length = 0;

    memcpy(header, binary, sizeof(u_int64_t));
    *header = ntohll(*header);
    binary = binary + sizeof(u_int64_t);
    length = length + sizeof(u_int64_t);

    return length;
}

typedef struct {
    u_int64_t value;
    struct List_u_int64_t* next;
} List_u_int64_t;

u_int32_t parse_list_u_int64_t(u_int8_t* binary, List_u_int64_t* header){
    u_int32_t length = 0;

    length = parse_u_int64_t(binary, &(header->value));
    binary = binary + sizeof(u_int64_t);

    return length;
}

typedef struct {
    u_int32_t len;
    u_int8_t* value;
} Length_Value;

typedef struct {
    Length_Value value;
    struct List_Length_Value* next;
} List_Length_Value;

u_int32_t parse_Length_Value(u_int8_t* binary, Length_Value* header){
    u_int32_t length = 0;
    u_int32_t struct_length = 0;

    struct_length = parse_u_int32_t(binary, &(header->len));
    binary = binary + struct_length;
    length = length + struct_length;

    if(header->len > 0){
        header->value = (u_int8_t*)malloc(header->len);
        memcpy(header->value, binary, (header->len));
        binary = binary + header->len;
        length = length + header->len;
    }

    return length;
}

u_int32_t parse_list_Length_Value(u_int8_t* binary, List_Length_Value* header){
    u_int32_t length = 0;
    u_int32_t struct_length = 0;

    struct_length = parse_u_int32_t(binary, &(header->value.len));
    binary = binary + struct_length;
    length = length + struct_length;

    if(header->value.len > 0){
        header->value.value = (u_int8_t*)malloc(header->value.len);
        memcpy((header->value.value), binary, (header->value.len));
        header->value.value[header->value.len] = '\0';
        binary = binary + header->value.len;
        length = length + header->value.len;
    }

    return length;
}

void print_Length_Value(Length_Value* header){
    printf("len %d \n",header->len);
    if(header->len != 0){
        int c = 0;
        for (int i = 0 ; i < (header->len/8) + 1;i++){
            for (int n = 0 ; n < 8;n++){
                printf("%02x",header->value[i * 8 + n]);
                c +=  1;
                if (c==header->len){
                    break;
                }
            }
            printf("\n");
        }
    }
}

void free_value_of_Length_Value(Length_Value * header){
    if(header->value == NULL || header->len == 0){
        return;
    }
    free(header->value);
}

void free_list_Length_Value(List_Length_Value * header){
    if(header == NULL){
        return;
    }
    //It does not have to free (header->next).
    //(header->next) is define by python code, so (header->next->next) is managed by c 
    free_value_of_Length_Value(header);
    free(header);
}

void free_Length_Value(Length_Value * header){
    if(header == NULL){
        return;
    }
    free_value_of_Length_Value(header);
}

typedef struct {
    u_int16_t len;
    u_int8_t* value;
} u_int256_t;

typedef struct {
    u_int256_t value;
    struct List_u_int256_t* next;
} List_u_int256_t;

u_int32_t parse_u_int256_t(u_int8_t* binary, u_int256_t* header){
    u_int32_t length = 0;
    u_int32_t struct_length = 0;

    struct_length = parse_u_int16_t(binary, &(header->len));
    binary = binary + struct_length;
    length = length + struct_length;

    if(header->len > 0){
        header->value = (u_int8_t*)malloc(header->len);
        memcpy(header->value, binary, (header->len));
        binary = binary + header->len;
        length = length + header->len;
    }

    return length;
}

u_int32_t parse_list_u_int256_t(u_int8_t* binary, List_u_int256_t* header){
    u_int32_t length = 0;
    u_int32_t struct_length = 0;

    struct_length = parse_u_int16_t(binary, &(header->value.len));
    binary = binary + struct_length;
    length = length + struct_length;

    if(header->value.len > 0){
        header->value.value = (u_int8_t*)malloc(header->value.len);
        memcpy((header->value.value), binary, (header->value.len));
        header->value.value[header->value.len] = '\0';
        binary = binary + header->value.len;
        length = length + header->value.len;
    }

    return length;
}

void print_u_int256_t(u_int256_t* header){
    printf("len %d \n",header->len);
    if(header->len != 0){
        int c = 0;
        for (int i = 0 ; i < (header->len/8) + 1;i++){
            for (int n = 0 ; n < 8;n++){
                printf("%02x",header->value[i * 8 + n]);
                c +=  1;
                if (c==header->len){
                    break;
                }
            }
            printf("\n");
        }
    }
}

void free_value_of_u_int256_t(u_int256_t * header){
    if(header->value == NULL || header->len == 0){
        return;
    }
    free(header->value);
}

void free_list_u_int256_t(List_u_int256_t * header){
    if(header == NULL){
        return;
    }
    //It does not have to free (header->next).
    //(header->next) is define by python code, so (header->next->next) is managed by c 
    free_value_of_u_int256_t(header);
    free(header);
}

void free_u_int256_t(u_int256_t * header){
    if(header == NULL){
        return;
    }
    free_value_of_u_int256_t(header);
}

typedef struct {
    u_int256_t asset_group_id;
    u_int256_t transaction_id;
} Cross_Ref;

typedef struct {
    Cross_Ref value;
    struct List_Cross_Ref* next;
} List_Cross_Ref;

u_int32_t parse_Cross_Ref(u_int8_t* binary, Cross_Ref* header){
    u_int32_t length = 0;
    u_int32_t struct_length = 0;

    struct_length = parse_u_int256_t(binary, &(header->asset_group_id));
    binary = binary + struct_length;
    length = length + struct_length;

    struct_length = parse_u_int256_t(binary, &(header->transaction_id));
    binary = binary + struct_length;
    length = length + struct_length;

    return length;
}

u_int32_t parse_list_Cross_Ref(u_int8_t* binary, List_Cross_Ref* header){
    u_int32_t length = 0;
    u_int32_t struct_length = 0;

    struct_length = parse_u_int256_t(binary, &(header->value.asset_group_id));
    binary = binary + struct_length;
    length = length + struct_length;

    struct_length = parse_u_int256_t(binary, &(header->value.transaction_id));
    binary = binary + struct_length;
    length = length + struct_length;

    return length;
}

void print_Cross_Ref(Cross_Ref* header){
    print_u_int256_t(&(header->asset_group_id));
    print_u_int256_t(&(header->transaction_id));
}

void free_list_Cross_Ref(List_Cross_Ref * header){
    if(header == NULL){
        return;
    }
    //It does not have to free (header->next).
    //(header->next) is define by python code, so (header->next->next) is managed by c 
    free(header);
}

void free_Cross_Ref(Cross_Ref * header){
    if(header == NULL){
        return;
    }
    free_u_int256_t(&(header->asset_group_id));
    free_u_int256_t(&(header->transaction_id));
}

typedef struct {
    u_int256_t asset_id;
    u_int256_t user_id;
    u_int16_t nonce_length;
    u_int8_t* nonce;
    u_int32_t asset_file_size;
    u_int256_t asset_file_digest;
    u_int16_t body_size;
    u_int8_t* body;
} Asset_Base;

typedef struct {
    Asset_Base value;
    struct List_Asset_Base* next;
} List_Asset_Base;

u_int32_t parse_Asset_Base(u_int8_t* binary, Asset_Base* header){
    u_int32_t length = 0;
    u_int32_t struct_length = 0;

    struct_length = parse_u_int256_t(binary, &(header->asset_id));
    binary = binary + struct_length;
    length = length + struct_length;

    struct_length = parse_u_int256_t(binary, &(header->user_id));
    binary = binary + struct_length;
    length = length + struct_length;

    struct_length = parse_u_int16_t(binary, &(header->nonce_length));
    binary = binary + struct_length;
    length = length + struct_length;

    if(header->nonce_length > 0){
        header->nonce = (u_int8_t*)malloc(header->nonce_length);
        memcpy(header->nonce, binary, (header->nonce_length));
        binary = binary + header->nonce_length;
        length = length + header->nonce_length;
    }

    struct_length = parse_u_int32_t(binary, &(header->asset_file_size));
    binary = binary + struct_length;
    length = length + struct_length;

    struct_length = parse_u_int256_t(binary, &(header->asset_file_digest));
    binary = binary + struct_length;
    length = length + struct_length;

    struct_length = parse_u_int16_t(binary, &(header->body_size));
    binary = binary + struct_length;
    length = length + struct_length;

    if(header->body_size > 0){
        header->body = (u_int8_t*)malloc(header->body_size);
        memcpy(header->body, binary, (header->body_size));
        binary = binary + header->body_size;
        length = length + header->body_size;
    }

    return length;
}

u_int32_t parse_list_Asset_Base(u_int8_t* binary, List_Asset_Base* header){
    u_int32_t length = 0;
    u_int32_t struct_length = 0;

    struct_length = parse_u_int256_t(binary, &(header->value.asset_id));
    binary = binary + struct_length;
    length = length + struct_length;

    struct_length = parse_u_int256_t(binary, &(header->value.user_id));
    binary = binary + struct_length;
    length = length + struct_length;

    struct_length = parse_u_int16_t(binary, &(header->value.nonce_length));
    binary = binary + struct_length;
    length = length + struct_length;

    if(header->value.nonce_length > 0){
        header->value.nonce = (u_int8_t*)malloc(header->value.nonce_length);
        memcpy((header->value.nonce), binary, (header->value.nonce_length));
        header->value.nonce[header->value.nonce_length] = '\0';
        binary = binary + header->value.nonce_length;
        length = length + header->value.nonce_length;
    }

    struct_length = parse_u_int32_t(binary, &(header->value.asset_file_size));
    binary = binary + struct_length;
    length = length + struct_length;

    struct_length = parse_u_int256_t(binary, &(header->value.asset_file_digest));
    binary = binary + struct_length;
    length = length + struct_length;

    struct_length = parse_u_int16_t(binary, &(header->value.body_size));
    binary = binary + struct_length;
    length = length + struct_length;

    if(header->value.body_size > 0){
        header->value.body = (u_int8_t*)malloc(header->value.body_size);
        memcpy((header->value.body), binary, (header->value.body_size));
        header->value.body[header->value.body_size] = '\0';
        binary = binary + header->value.body_size;
        length = length + header->value.body_size;
    }

    return length;
}

void print_Asset_Base(Asset_Base* header){
    print_u_int256_t(&(header->asset_id));
    print_u_int256_t(&(header->user_id));
    printf("nonce_length %d \n",header->nonce_length);
    if(header->nonce_length != 0){
        int c = 0;
        for (int i = 0 ; i < (header->nonce_length/8) + 1;i++){
            for (int n = 0 ; n < 8;n++){
                printf("%02x",header->nonce[i * 8 + n]);
                c +=  1;
                if (c==header->nonce_length){
                    break;
                }
            }
            printf("\n");
        }
    }
    printf("asset_file_size %d \n",header->asset_file_size);
    print_u_int256_t(&(header->asset_file_digest));
    printf("body_size %d \n",header->body_size);
    if(header->body_size != 0){
        int c = 0;
        for (int i = 0 ; i < (header->body_size/8) + 1;i++){
            for (int n = 0 ; n < 8;n++){
                printf("%02x",header->body[i * 8 + n]);
                c +=  1;
                if (c==header->body_size){
                    break;
                }
            }
            printf("\n");
        }
    }
}

void free_nonce_of_Asset_Base(Asset_Base * header){
    if(header->nonce == NULL || header->nonce_length == 0){
        return;
    }
    free(header->nonce);
}

void free_body_of_Asset_Base(Asset_Base * header){
    if(header->body == NULL || header->body_size == 0){
        return;
    }
    free(header->body);
}

void free_list_Asset_Base(List_Asset_Base * header){
    if(header == NULL){
        return;
    }
    //It does not have to free (header->next).
    //(header->next) is define by python code, so (header->next->next) is managed by c 
    free_nonce_of_Asset_Base(header);
    free_body_of_Asset_Base(header);
    free(header);
}

void free_Asset_Base(Asset_Base * header){
    if(header == NULL){
        return;
    }
    free_u_int256_t(&(header->asset_id));
    free_u_int256_t(&(header->user_id));
    free_nonce_of_Asset_Base(header);
    free_u_int256_t(&(header->asset_file_digest));
    free_body_of_Asset_Base(header);
}

typedef struct {
    u_int256_t asset_id;
    u_int256_t user_id;
    u_int16_t nonce_length;
    u_int8_t* nonce;
    u_int32_t asset_file_size;
    u_int256_t asset_file_digest;
    u_int16_t body_size;
    u_int8_t* body;
} Asset;

typedef struct {
    Asset value;
    struct List_Asset* next;
} List_Asset;

u_int32_t parse_Asset(u_int8_t* binary, Asset* header){
    u_int32_t length = 0;
    u_int32_t struct_length = 0;

    struct_length = parse_u_int256_t(binary, &(header->asset_id));
    binary = binary + struct_length;
    length = length + struct_length;

    struct_length = parse_u_int256_t(binary, &(header->user_id));
    binary = binary + struct_length;
    length = length + struct_length;

    struct_length = parse_u_int16_t(binary, &(header->nonce_length));
    binary = binary + struct_length;
    length = length + struct_length;

    if(header->nonce_length > 0){
        header->nonce = (u_int8_t*)malloc(header->nonce_length);
        memcpy(header->nonce, binary, (header->nonce_length));
        binary = binary + header->nonce_length;
        length = length + header->nonce_length;
    }

    struct_length = parse_u_int32_t(binary, &(header->asset_file_size));
    binary = binary + struct_length;
    length = length + struct_length;

    struct_length = parse_u_int256_t(binary, &(header->asset_file_digest));
    binary = binary + struct_length;
    length = length + struct_length;

    struct_length = parse_u_int16_t(binary, &(header->body_size));
    binary = binary + struct_length;
    length = length + struct_length;

    if(header->body_size > 0){
        header->body = (u_int8_t*)malloc(header->body_size);
        memcpy(header->body, binary, (header->body_size));
        binary = binary + header->body_size;
        length = length + header->body_size;
    }

    return length;
}

u_int32_t parse_list_Asset(u_int8_t* binary, List_Asset* header){
    u_int32_t length = 0;
    u_int32_t struct_length = 0;

    struct_length = parse_u_int256_t(binary, &(header->value.asset_id));
    binary = binary + struct_length;
    length = length + struct_length;

    struct_length = parse_u_int256_t(binary, &(header->value.user_id));
    binary = binary + struct_length;
    length = length + struct_length;

    struct_length = parse_u_int16_t(binary, &(header->value.nonce_length));
    binary = binary + struct_length;
    length = length + struct_length;

    if(header->value.nonce_length > 0){
        header->value.nonce = (u_int8_t*)malloc(header->value.nonce_length);
        memcpy((header->value.nonce), binary, (header->value.nonce_length));
        header->value.nonce[header->value.nonce_length] = '\0';
        binary = binary + header->value.nonce_length;
        length = length + header->value.nonce_length;
    }

    struct_length = parse_u_int32_t(binary, &(header->value.asset_file_size));
    binary = binary + struct_length;
    length = length + struct_length;

    struct_length = parse_u_int256_t(binary, &(header->value.asset_file_digest));
    binary = binary + struct_length;
    length = length + struct_length;

    struct_length = parse_u_int16_t(binary, &(header->value.body_size));
    binary = binary + struct_length;
    length = length + struct_length;

    if(header->value.body_size > 0){
        header->value.body = (u_int8_t*)malloc(header->value.body_size);
        memcpy((header->value.body), binary, (header->value.body_size));
        header->value.body[header->value.body_size] = '\0';
        binary = binary + header->value.body_size;
        length = length + header->value.body_size;
    }

    return length;
}

void print_Asset(Asset* header){
    print_u_int256_t(&(header->asset_id));
    print_u_int256_t(&(header->user_id));
    printf("nonce_length %d \n",header->nonce_length);
    if(header->nonce_length != 0){
        int c = 0;
        for (int i = 0 ; i < (header->nonce_length/8) + 1;i++){
            for (int n = 0 ; n < 8;n++){
                printf("%02x",header->nonce[i * 8 + n]);
                c +=  1;
                if (c==header->nonce_length){
                    break;
                }
            }
            printf("\n");
        }
    }
    printf("asset_file_size %d \n",header->asset_file_size);
    print_u_int256_t(&(header->asset_file_digest));
    printf("body_size %d \n",header->body_size);
    if(header->body_size != 0){
        int c = 0;
        for (int i = 0 ; i < (header->body_size/8) + 1;i++){
            for (int n = 0 ; n < 8;n++){
                printf("%02x",header->body[i * 8 + n]);
                c +=  1;
                if (c==header->body_size){
                    break;
                }
            }
            printf("\n");
        }
    }
}

void free_nonce_of_Asset(Asset * header){
    if(header->nonce == NULL || header->nonce_length == 0){
        return;
    }
    free(header->nonce);
}

void free_body_of_Asset(Asset * header){
    if(header->body == NULL || header->body_size == 0){
        return;
    }
    free(header->body);
}

void free_list_Asset(List_Asset * header){
    if(header == NULL){
        return;
    }
    //It does not have to free (header->next).
    //(header->next) is define by python code, so (header->next->next) is managed by c 
    free_nonce_of_Asset(header);
    free_body_of_Asset(header);
    free(header);
}

void free_Asset(Asset * header){
    if(header == NULL){
        return;
    }
    free_u_int256_t(&(header->asset_id));
    free_u_int256_t(&(header->user_id));
    free_nonce_of_Asset(header);
    free_u_int256_t(&(header->asset_file_digest));
    free_body_of_Asset(header);
}

typedef struct {
    u_int256_t asset_group_id;
    u_int256_t transaction_id;
    u_int16_t event_index;
    u_int16_t signature_indice_num;
    List_u_int16_t* signature_indices;
} Reference;

typedef struct {
    Reference value;
    struct List_Reference* next;
} List_Reference;

u_int32_t parse_Reference(u_int8_t* binary, Reference* header){
    u_int32_t length = 0;
    u_int32_t struct_length = 0;

    struct_length = parse_u_int256_t(binary, &(header->asset_group_id));
    binary = binary + struct_length;
    length = length + struct_length;

    struct_length = parse_u_int256_t(binary, &(header->transaction_id));
    binary = binary + struct_length;
    length = length + struct_length;

    struct_length = parse_u_int16_t(binary, &(header->event_index));
    binary = binary + struct_length;
    length = length + struct_length;

    struct_length = parse_u_int16_t(binary, &(header->signature_indice_num));
    binary = binary + struct_length;
    length = length + struct_length;

    if(header->signature_indice_num > 0){
        List_u_int16_t* current = header->signature_indices;
        for(int i = 0; i < header->signature_indice_num; i++){
            List_u_int16_t* instance = (List_u_int16_t*)malloc(sizeof(List_u_int16_t));
            struct_length = parse_u_int16_t(binary, &(instance->value));
            binary = binary + struct_length;
            length = length + struct_length;
            current->next = instance;
            current = current->next;
        }
    }

    return length;
}

u_int32_t parse_list_Reference(u_int8_t* binary, List_Reference* header){
    u_int32_t length = 0;
    u_int32_t struct_length = 0;

    struct_length = parse_u_int256_t(binary, &(header->value.asset_group_id));
    binary = binary + struct_length;
    length = length + struct_length;

    struct_length = parse_u_int256_t(binary, &(header->value.transaction_id));
    binary = binary + struct_length;
    length = length + struct_length;

    struct_length = parse_u_int16_t(binary, &(header->value.event_index));
    binary = binary + struct_length;
    length = length + struct_length;

    struct_length = parse_u_int16_t(binary, &(header->value.signature_indice_num));
    binary = binary + struct_length;
    length = length + struct_length;

    if(header->value.signature_indice_num > 0){
        List_u_int16_t* current = header->value.signature_indices;
        for(int i = 0; i < header->value.signature_indice_num; i++){
            List_u_int16_t* instance = (List_u_int16_t*)malloc(sizeof(List_u_int16_t));
            struct_length = parse_u_int16_t(binary, &(instance->value));
            binary = binary + struct_length;
            length = length + struct_length;
            current->next = instance;
            current = current->next;
        }
    }

    return length;
}

void print_Reference(Reference* header){
    print_u_int256_t(&(header->asset_group_id));
    print_u_int256_t(&(header->transaction_id));
    printf("event_index %d \n",header->event_index);
    printf("signature_indice_num %d \n",header->signature_indice_num);
    printf("signature_indices %d \n",header->signature_indices);
}

void free_signature_indices_of_Reference(Reference * header){
    if(header->signature_indices == NULL){
        return;
    }
    if (header->signature_indice_num > 0){
        List_u_int16_t* current = header->signature_indices->next;
        List_u_int16_t* next;
        for(int i = 0; i < header->signature_indice_num; i++){
            next = current->next;
            free(current);
            current = next;
        }
    }
}

void free_list_Reference(List_Reference * header){
    if(header == NULL){
        return;
    }
    //It does not have to free (header->next).
    //(header->next) is define by python code, so (header->next->next) is managed by c 
    free_signature_indices_of_Reference(header);
    free(header);
}

void free_Reference(Reference * header){
    if(header == NULL){
        return;
    }
    free_u_int256_t(&(header->asset_group_id));
    free_u_int256_t(&(header->transaction_id));
    free_signature_indices_of_Reference(header);
}

typedef struct {
    Length_Value asset_group_id;
    u_int16_t reference_num;
    List_u_int16_t* reference_indices;
    u_int16_t mandatory_approver_num;
    List_Length_Value* mandatory_approvers;
    u_int16_t option_approval_numerator;
    u_int16_t option_approval_denominator;
    List_Length_Value* option_approvers;
    u_int32_t asset_length;
    u_int8_t* asset;
} Event;

typedef struct {
    Event value;
    struct List_Event* next;
} List_Event;

u_int32_t parse_Event(u_int8_t* binary, Event* header){
    u_int32_t length = 0;
    u_int32_t struct_length = 0;

    struct_length = parse_Length_Value(binary, &(header->asset_group_id));
    binary = binary + struct_length;
    length = length + struct_length;

    struct_length = parse_u_int16_t(binary, &(header->reference_num));
    binary = binary + struct_length;
    length = length + struct_length;

    if(header->reference_num > 0){
        List_u_int16_t* current = header->reference_indices;
        for(int i = 0; i < header->reference_num; i++){
            List_u_int16_t* instance = (List_u_int16_t*)malloc(sizeof(List_u_int16_t));
            struct_length = parse_u_int16_t(binary, &(instance->value));
            binary = binary + struct_length;
            length = length + struct_length;
            current->next = instance;
            current = current->next;
        }
    }

    struct_length = parse_u_int16_t(binary, &(header->mandatory_approver_num));
    binary = binary + struct_length;
    length = length + struct_length;

    if(header->mandatory_approver_num > 0){
        List_Length_Value* current = header->mandatory_approvers;
        for(int i = 0; i < header->mandatory_approver_num; i++){
            List_Length_Value* instance = (List_Length_Value*)malloc(sizeof(List_Length_Value));
            struct_length = parse_Length_Value(binary, &(instance->value));
            binary = binary + struct_length;
            length = length + struct_length;
            current->next = instance;
            current = current->next;
        }
    }

    struct_length = parse_u_int16_t(binary, &(header->option_approval_numerator));
    binary = binary + struct_length;
    length = length + struct_length;

    struct_length = parse_u_int16_t(binary, &(header->option_approval_denominator));
    binary = binary + struct_length;
    length = length + struct_length;

    if(header->option_approval_denominator > 0){
        List_Length_Value* current = header->option_approvers;
        for(int i = 0; i < header->option_approval_denominator; i++){
            List_Length_Value* instance = (List_Length_Value*)malloc(sizeof(List_Length_Value));
            struct_length = parse_Length_Value(binary, &(instance->value));
            binary = binary + struct_length;
            length = length + struct_length;
            current->next = instance;
            current = current->next;
        }
    }

    struct_length = parse_u_int32_t(binary, &(header->asset_length));
    binary = binary + struct_length;
    length = length + struct_length;

    if(header->asset_length > 0){
        header->asset = (u_int8_t*)malloc(header->asset_length);
        memcpy(header->asset, binary, (header->asset_length));
        binary = binary + header->asset_length;
        length = length + header->asset_length;
    }

    return length;
}

u_int32_t parse_list_Event(u_int8_t* binary, List_Event* header){
    u_int32_t length = 0;
    u_int32_t struct_length = 0;

    struct_length = parse_Length_Value(binary, &(header->value.asset_group_id));
    binary = binary + struct_length;
    length = length + struct_length;

    struct_length = parse_u_int16_t(binary, &(header->value.reference_num));
    binary = binary + struct_length;
    length = length + struct_length;

    if(header->value.reference_num > 0){
        List_u_int16_t* current = header->value.reference_indices;
        for(int i = 0; i < header->value.reference_num; i++){
            List_u_int16_t* instance = (List_u_int16_t*)malloc(sizeof(List_u_int16_t));
            struct_length = parse_u_int16_t(binary, &(instance->value));
            binary = binary + struct_length;
            length = length + struct_length;
            current->next = instance;
            current = current->next;
        }
    }

    struct_length = parse_u_int16_t(binary, &(header->value.mandatory_approver_num));
    binary = binary + struct_length;
    length = length + struct_length;

    if(header->value.mandatory_approver_num > 0){
        List_Length_Value* current = header->value.mandatory_approvers;
        for(int i = 0; i < header->value.mandatory_approver_num; i++){
            List_Length_Value* instance = (List_Length_Value*)malloc(sizeof(List_Length_Value));
            struct_length = parse_Length_Value(binary, &(instance->value));
            binary = binary + struct_length;
            length = length + struct_length;
            current->next = instance;
            current = current->next;
        }
    }

    struct_length = parse_u_int16_t(binary, &(header->value.option_approval_numerator));
    binary = binary + struct_length;
    length = length + struct_length;

    struct_length = parse_u_int16_t(binary, &(header->value.option_approval_denominator));
    binary = binary + struct_length;
    length = length + struct_length;

    if(header->value.option_approval_denominator > 0){
        List_Length_Value* current = header->value.option_approvers;
        for(int i = 0; i < header->value.option_approval_denominator; i++){
            List_Length_Value* instance = (List_Length_Value*)malloc(sizeof(List_Length_Value));
            struct_length = parse_Length_Value(binary, &(instance->value));
            binary = binary + struct_length;
            length = length + struct_length;
            current->next = instance;
            current = current->next;
        }
    }

    struct_length = parse_u_int32_t(binary, &(header->value.asset_length));
    binary = binary + struct_length;
    length = length + struct_length;

    if(header->value.asset_length > 0){
        header->value.asset = (u_int8_t*)malloc(header->value.asset_length);
        memcpy((header->value.asset), binary, (header->value.asset_length));
        header->value.asset[header->value.asset_length] = '\0';
        binary = binary + header->value.asset_length;
        length = length + header->value.asset_length;
    }

    return length;
}

void add_to_mandatory_approvers_list_of_Event(Event* head, int length, void* value){
    List_Length_Value * current = head->mandatory_approvers;
    if(head->mandatory_approver_num == 0){
        head->mandatory_approver_num= head->mandatory_approver_num + 1;
        List_Length_Value * v = (List_Length_Value * )malloc(sizeof(List_Length_Value));
        v->value.len = length;
        v->value.value = (void * )malloc(length);
        memcpy(v->value.value, value, length);
        current->next = v;
        return;
    }
    for (int i = 0;i < head->mandatory_approver_num;i++){
        current = current->next;
        if (head->mandatory_approver_num - 1 == i){
            head->mandatory_approver_num= head->mandatory_approver_num + 1;
            List_Length_Value * v = (List_Length_Value * )malloc(sizeof(List_Length_Value));
            v->value.len = length;
            v->value.value = (void * )malloc(length);
            memcpy(v->value.value, value, length);
            current->next = v;
            return;
        }
    }
}

void add_to_option_approvers_list_of_Event(Event* head, int length, void* value){
    List_Length_Value * current = head->option_approvers;
    if(head->option_approval_denominator == 0){
        head->option_approval_denominator= head->option_approval_denominator + 1;
        List_Length_Value * v = (List_Length_Value * )malloc(sizeof(List_Length_Value));
        v->value.len = length;
        v->value.value = (void * )malloc(length);
        memcpy(v->value.value, value, length);
        current->next = v;
        return;
    }
    for (int i = 0;i < head->option_approval_denominator;i++){
        current = current->next;
        if (head->option_approval_denominator - 1 == i){
            head->option_approval_denominator= head->option_approval_denominator + 1;
            List_Length_Value * v = (List_Length_Value * )malloc(sizeof(List_Length_Value));
            v->value.len = length;
            v->value.value = (void * )malloc(length);
            memcpy(v->value.value, value, length);
            current->next = v;
            return;
        }
    }
}

void print_Event(Event* header){
    print_Length_Value(&(header->asset_group_id));
    printf("reference_num %d \n",header->reference_num);
    printf("reference_indices %d \n",header->reference_indices);
    printf("mandatory_approver_num %d \n",header->mandatory_approver_num);
    print_Length_Value((header->mandatory_approvers));
    printf("option_approval_numerator %d \n",header->option_approval_numerator);
    printf("option_approval_denominator %d \n",header->option_approval_denominator);
    print_Length_Value((header->option_approvers));
    printf("asset_length %d \n",header->asset_length);
    if(header->asset_length != 0){
        int c = 0;
        for (int i = 0 ; i < (header->asset_length/8) + 1;i++){
            for (int n = 0 ; n < 8;n++){
                printf("%02x",header->asset[i * 8 + n]);
                c +=  1;
                if (c==header->asset_length){
                    break;
                }
            }
            printf("\n");
        }
    }
}

void free_reference_indices_of_Event(Event * header){
    if(header->reference_indices == NULL){
        return;
    }
    if (header->reference_num > 0){
        List_u_int16_t* current = header->reference_indices->next;
        List_u_int16_t* next;
        for(int i = 0; i < header->reference_num; i++){
            next = current->next;
            free(current);
            current = next;
        }
    }
}

void free_mandatory_approvers_of_Event(Event * header){
    if(header->mandatory_approvers == NULL){
        return;
    }
    if (header->mandatory_approver_num > 0){
        List_Length_Value* current = header->mandatory_approvers->next;
        List_Length_Value* next;
        for(int i = 0; i < header->mandatory_approver_num; i++){
            next = current->next;
            free_list_Length_Value(current);
            current = next;
        }
    }
}

void free_option_approvers_of_Event(Event * header){
    if(header->option_approvers == NULL){
        return;
    }
    if (header->option_approval_denominator > 0){
        List_Length_Value* current = header->option_approvers->next;
        List_Length_Value* next;
        for(int i = 0; i < header->option_approval_denominator; i++){
            next = current->next;
            free_list_Length_Value(current);
            current = next;
        }
    }
}

void free_asset_of_Event(Event * header){
    if(header->asset == NULL || header->asset_length == 0){
        return;
    }
    free(header->asset);
}

void free_list_Event(List_Event * header){
    if(header == NULL){
        return;
    }
    //It does not have to free (header->next).
    //(header->next) is define by python code, so (header->next->next) is managed by c 
    free_reference_indices_of_Event(header);
    free_mandatory_approvers_of_Event(header);
    free_option_approvers_of_Event(header);
    free_asset_of_Event(header);
    free(header);
}

void free_Event(Event * header){
    if(header == NULL){
        return;
    }
    free_Length_Value(&(header->asset_group_id));
    free_reference_indices_of_Event(header);
    free_mandatory_approvers_of_Event(header);
    free_option_approvers_of_Event(header);
    free_asset_of_Event(header);
}

typedef struct {
    u_int32_t type;
    u_int32_t public_key_length;
    u_int8_t* public_key;
    u_int32_t signature_length;
    u_int8_t* signature;
} Signature;

typedef struct {
    Signature value;
    struct List_Signature* next;
} List_Signature;

u_int32_t parse_Signature(u_int8_t* binary, Signature* header){
    u_int32_t length = 0;
    u_int32_t struct_length = 0;

    struct_length = parse_u_int32_t(binary, &(header->type));
    binary = binary + struct_length;
    length = length + struct_length;

    struct_length = parse_u_int32_t(binary, &(header->public_key_length));
    binary = binary + struct_length;
    length = length + struct_length;

    if(header->public_key_length > 0){
        header->public_key = (u_int8_t*)malloc(header->public_key_length);
        memcpy(header->public_key, binary, (header->public_key_length));
        binary = binary + header->public_key_length;
        length = length + header->public_key_length;
    }

    struct_length = parse_u_int32_t(binary, &(header->signature_length));
    binary = binary + struct_length;
    length = length + struct_length;

    if(header->signature_length > 0){
        header->signature = (u_int8_t*)malloc(header->signature_length);
        memcpy(header->signature, binary, (header->signature_length));
        binary = binary + header->signature_length;
        length = length + header->signature_length;
    }

    return length;
}

u_int32_t parse_list_Signature(u_int8_t* binary, List_Signature* header){
    u_int32_t length = 0;
    u_int32_t struct_length = 0;

    struct_length = parse_u_int32_t(binary, &(header->value.type));
    binary = binary + struct_length;
    length = length + struct_length;

    struct_length = parse_u_int32_t(binary, &(header->value.public_key_length));
    binary = binary + struct_length;
    length = length + struct_length;

    if(header->value.public_key_length > 0){
        header->value.public_key = (u_int8_t*)malloc(header->value.public_key_length);
        memcpy((header->value.public_key), binary, (header->value.public_key_length));
        header->value.public_key[header->value.public_key_length] = '\0';
        binary = binary + header->value.public_key_length;
        length = length + header->value.public_key_length;
    }

    struct_length = parse_u_int32_t(binary, &(header->value.signature_length));
    binary = binary + struct_length;
    length = length + struct_length;

    if(header->value.signature_length > 0){
        header->value.signature = (u_int8_t*)malloc(header->value.signature_length);
        memcpy((header->value.signature), binary, (header->value.signature_length));
        header->value.signature[header->value.signature_length] = '\0';
        binary = binary + header->value.signature_length;
        length = length + header->value.signature_length;
    }

    return length;
}

void print_Signature(Signature* header){
    printf("type %d \n",header->type);
    printf("public_key_length %d \n",header->public_key_length);
    if(header->public_key_length != 0){
        int c = 0;
        for (int i = 0 ; i < (header->public_key_length/8) + 1;i++){
            for (int n = 0 ; n < 8;n++){
                printf("%02x",header->public_key[i * 8 + n]);
                c +=  1;
                if (c==header->public_key_length){
                    break;
                }
            }
            printf("\n");
        }
    }
    printf("signature_length %d \n",header->signature_length);
    if(header->signature_length != 0){
        int c = 0;
        for (int i = 0 ; i < (header->signature_length/8) + 1;i++){
            for (int n = 0 ; n < 8;n++){
                printf("%02x",header->signature[i * 8 + n]);
                c +=  1;
                if (c==header->signature_length){
                    break;
                }
            }
            printf("\n");
        }
    }
}

void free_public_key_of_Signature(Signature * header){
    if(header->public_key == NULL || header->public_key_length == 0){
        return;
    }
    free(header->public_key);
}

void free_signature_of_Signature(Signature * header){
    if(header->signature == NULL || header->signature_length == 0){
        return;
    }
    free(header->signature);
}

void free_list_Signature(List_Signature * header){
    if(header == NULL){
        return;
    }
    //It does not have to free (header->next).
    //(header->next) is define by python code, so (header->next->next) is managed by c 
    free_public_key_of_Signature(header);
    free_signature_of_Signature(header);
    free(header);
}

void free_Signature(Signature * header){
    if(header == NULL){
        return;
    }
    free_public_key_of_Signature(header);
    free_signature_of_Signature(header);
}

typedef struct {
    u_int256_t transaction_base_digest;
    u_int16_t cross_ref_num;
    List_Length_Value* cross_refs;
} Intermediate;

typedef struct {
    Intermediate value;
    struct List_Intermediate* next;
} List_Intermediate;

u_int32_t parse_Intermediate(u_int8_t* binary, Intermediate* header){
    u_int32_t length = 0;
    u_int32_t struct_length = 0;

    struct_length = parse_u_int256_t(binary, &(header->transaction_base_digest));
    binary = binary + struct_length;
    length = length + struct_length;

    struct_length = parse_u_int16_t(binary, &(header->cross_ref_num));
    binary = binary + struct_length;
    length = length + struct_length;

    if(header->cross_ref_num > 0){
        List_Length_Value* current = header->cross_refs;
        for(int i = 0; i < header->cross_ref_num; i++){
            List_Length_Value* instance = (List_Length_Value*)malloc(sizeof(List_Length_Value));
            struct_length = parse_Length_Value(binary, &(instance->value));
            binary = binary + struct_length;
            length = length + struct_length;
            current->next = instance;
            current = current->next;
        }
    }

    return length;
}

u_int32_t parse_list_Intermediate(u_int8_t* binary, List_Intermediate* header){
    u_int32_t length = 0;
    u_int32_t struct_length = 0;

    struct_length = parse_u_int256_t(binary, &(header->value.transaction_base_digest));
    binary = binary + struct_length;
    length = length + struct_length;

    struct_length = parse_u_int16_t(binary, &(header->value.cross_ref_num));
    binary = binary + struct_length;
    length = length + struct_length;

    if(header->value.cross_ref_num > 0){
        List_Length_Value* current = header->value.cross_refs;
        for(int i = 0; i < header->value.cross_ref_num; i++){
            List_Length_Value* instance = (List_Length_Value*)malloc(sizeof(List_Length_Value));
            struct_length = parse_Length_Value(binary, &(instance->value));
            binary = binary + struct_length;
            length = length + struct_length;
            current->next = instance;
            current = current->next;
        }
    }

    return length;
}

void add_to_cross_refs_list_of_Intermediate(Intermediate* head, int length, void* value){
    List_Length_Value * current = head->cross_refs;
    if(head->cross_ref_num == 0){
        head->cross_ref_num= head->cross_ref_num + 1;
        List_Length_Value * v = (List_Length_Value * )malloc(sizeof(List_Length_Value));
        v->value.len = length;
        v->value.value = (void * )malloc(length);
        memcpy(v->value.value, value, length);
        current->next = v;
        return;
    }
    for (int i = 0;i < head->cross_ref_num;i++){
        current = current->next;
        if (head->cross_ref_num - 1 == i){
            head->cross_ref_num= head->cross_ref_num + 1;
            List_Length_Value * v = (List_Length_Value * )malloc(sizeof(List_Length_Value));
            v->value.len = length;
            v->value.value = (void * )malloc(length);
            memcpy(v->value.value, value, length);
            current->next = v;
            return;
        }
    }
}

void print_Intermediate(Intermediate* header){
    print_u_int256_t(&(header->transaction_base_digest));
    printf("cross_ref_num %d \n",header->cross_ref_num);
    print_Length_Value((header->cross_refs));
}

void free_cross_refs_of_Intermediate(Intermediate * header){
    if(header->cross_refs == NULL){
        return;
    }
    if (header->cross_ref_num > 0){
        List_Length_Value* current = header->cross_refs->next;
        List_Length_Value* next;
        for(int i = 0; i < header->cross_ref_num; i++){
            next = current->next;
            free_list_Length_Value(current);
            current = next;
        }
    }
}

void free_list_Intermediate(List_Intermediate * header){
    if(header == NULL){
        return;
    }
    //It does not have to free (header->next).
    //(header->next) is define by python code, so (header->next->next) is managed by c 
    free_cross_refs_of_Intermediate(header);
    free(header);
}

void free_Intermediate(Intermediate * header){
    if(header == NULL){
        return;
    }
    free_u_int256_t(&(header->transaction_base_digest));
    free_cross_refs_of_Intermediate(header);
}

typedef struct {
    u_int32_t version;
    u_int64_t timestamp;
    u_int16_t event_num;
    List_Length_Value* events;
    u_int16_t reference_num;
    List_Length_Value* references;
} Transaction_Base;

typedef struct {
    Transaction_Base value;
    struct List_Transaction_Base* next;
} List_Transaction_Base;

u_int32_t parse_Transaction_Base(u_int8_t* binary, Transaction_Base* header){
    u_int32_t length = 0;
    u_int32_t struct_length = 0;

    struct_length = parse_u_int32_t(binary, &(header->version));
    binary = binary + struct_length;
    length = length + struct_length;

    struct_length = parse_u_int64_t(binary, &(header->timestamp));
    binary = binary + struct_length;
    length = length + struct_length;

    struct_length = parse_u_int16_t(binary, &(header->event_num));
    binary = binary + struct_length;
    length = length + struct_length;

    if(header->event_num > 0){
        List_Length_Value* current = header->events;
        for(int i = 0; i < header->event_num; i++){
            List_Length_Value* instance = (List_Length_Value*)malloc(sizeof(List_Length_Value));
            struct_length = parse_Length_Value(binary, &(instance->value));
            binary = binary + struct_length;
            length = length + struct_length;
            current->next = instance;
            current = current->next;
        }
    }

    struct_length = parse_u_int16_t(binary, &(header->reference_num));
    binary = binary + struct_length;
    length = length + struct_length;

    if(header->reference_num > 0){
        List_Length_Value* current = header->references;
        for(int i = 0; i < header->reference_num; i++){
            List_Length_Value* instance = (List_Length_Value*)malloc(sizeof(List_Length_Value));
            struct_length = parse_Length_Value(binary, &(instance->value));
            binary = binary + struct_length;
            length = length + struct_length;
            current->next = instance;
            current = current->next;
        }
    }

    return length;
}

u_int32_t parse_list_Transaction_Base(u_int8_t* binary, List_Transaction_Base* header){
    u_int32_t length = 0;
    u_int32_t struct_length = 0;

    struct_length = parse_u_int32_t(binary, &(header->value.version));
    binary = binary + struct_length;
    length = length + struct_length;

    struct_length = parse_u_int64_t(binary, &(header->value.timestamp));
    binary = binary + struct_length;
    length = length + struct_length;

    struct_length = parse_u_int16_t(binary, &(header->value.event_num));
    binary = binary + struct_length;
    length = length + struct_length;

    if(header->value.event_num > 0){
        List_Length_Value* current = header->value.events;
        for(int i = 0; i < header->value.event_num; i++){
            List_Length_Value* instance = (List_Length_Value*)malloc(sizeof(List_Length_Value));
            struct_length = parse_Length_Value(binary, &(instance->value));
            binary = binary + struct_length;
            length = length + struct_length;
            current->next = instance;
            current = current->next;
        }
    }

    struct_length = parse_u_int16_t(binary, &(header->value.reference_num));
    binary = binary + struct_length;
    length = length + struct_length;

    if(header->value.reference_num > 0){
        List_Length_Value* current = header->value.references;
        for(int i = 0; i < header->value.reference_num; i++){
            List_Length_Value* instance = (List_Length_Value*)malloc(sizeof(List_Length_Value));
            struct_length = parse_Length_Value(binary, &(instance->value));
            binary = binary + struct_length;
            length = length + struct_length;
            current->next = instance;
            current = current->next;
        }
    }

    return length;
}

void add_to_events_list_of_Transaction_Base(Transaction_Base* head, int length, void* value){
    List_Length_Value * current = head->events;
    if(head->event_num == 0){
        head->event_num= head->event_num + 1;
        List_Length_Value * v = (List_Length_Value * )malloc(sizeof(List_Length_Value));
        v->value.len = length;
        v->value.value = (void * )malloc(length);
        memcpy(v->value.value, value, length);
        current->next = v;
        return;
    }
    for (int i = 0;i < head->event_num;i++){
        current = current->next;
        if (head->event_num - 1 == i){
            head->event_num= head->event_num + 1;
            List_Length_Value * v = (List_Length_Value * )malloc(sizeof(List_Length_Value));
            v->value.len = length;
            v->value.value = (void * )malloc(length);
            memcpy(v->value.value, value, length);
            current->next = v;
            return;
        }
    }
}

void add_to_references_list_of_Transaction_Base(Transaction_Base* head, int length, void* value){
    List_Length_Value * current = head->references;
    if(head->reference_num == 0){
        head->reference_num= head->reference_num + 1;
        List_Length_Value * v = (List_Length_Value * )malloc(sizeof(List_Length_Value));
        v->value.len = length;
        v->value.value = (void * )malloc(length);
        memcpy(v->value.value, value, length);
        current->next = v;
        return;
    }
    for (int i = 0;i < head->reference_num;i++){
        current = current->next;
        if (head->reference_num - 1 == i){
            head->reference_num= head->reference_num + 1;
            List_Length_Value * v = (List_Length_Value * )malloc(sizeof(List_Length_Value));
            v->value.len = length;
            v->value.value = (void * )malloc(length);
            memcpy(v->value.value, value, length);
            current->next = v;
            return;
        }
    }
}

void print_Transaction_Base(Transaction_Base* header){
    printf("version %d \n",header->version);
    printf("timestamp %llu \n",header->timestamp);
    printf("event_num %d \n",header->event_num);
    print_Length_Value((header->events));
    printf("reference_num %d \n",header->reference_num);
    print_Length_Value((header->references));
}

void free_events_of_Transaction_Base(Transaction_Base * header){
    if(header->events == NULL){
        return;
    }
    if (header->event_num > 0){
        List_Length_Value* current = header->events->next;
        List_Length_Value* next;
        for(int i = 0; i < header->event_num; i++){
            next = current->next;
            free_list_Length_Value(current);
            current = next;
        }
    }
}

void free_references_of_Transaction_Base(Transaction_Base * header){
    if(header->references == NULL){
        return;
    }
    if (header->reference_num > 0){
        List_Length_Value* current = header->references->next;
        List_Length_Value* next;
        for(int i = 0; i < header->reference_num; i++){
            next = current->next;
            free_list_Length_Value(current);
            current = next;
        }
    }
}

void free_list_Transaction_Base(List_Transaction_Base * header){
    if(header == NULL){
        return;
    }
    //It does not have to free (header->next).
    //(header->next) is define by python code, so (header->next->next) is managed by c 
    free_events_of_Transaction_Base(header);
    free_references_of_Transaction_Base(header);
    free(header);
}

void free_Transaction_Base(Transaction_Base * header){
    if(header == NULL){
        return;
    }
    free_events_of_Transaction_Base(header);
    free_references_of_Transaction_Base(header);
}

typedef struct {
    u_int32_t version;
    u_int64_t timestamp;
    u_int16_t event_num;
    List_Length_Value* events;
    u_int16_t reference_num;
    List_Length_Value* references;
    u_int16_t cross_ref_num;
    List_Length_Value* cross_refs;
    u_int16_t signature_num;
    List_Length_Value* signatures;
} Transaction;

typedef struct {
    Transaction value;
    struct List_Transaction* next;
} List_Transaction;

u_int32_t parse_Transaction(u_int8_t* binary, Transaction* header){
    u_int32_t length = 0;
    u_int32_t struct_length = 0;

    struct_length = parse_u_int32_t(binary, &(header->version));
    binary = binary + struct_length;
    length = length + struct_length;

    struct_length = parse_u_int64_t(binary, &(header->timestamp));
    binary = binary + struct_length;
    length = length + struct_length;

    struct_length = parse_u_int16_t(binary, &(header->event_num));
    binary = binary + struct_length;
    length = length + struct_length;

    if(header->event_num > 0){
        List_Length_Value* current = header->events;
        for(int i = 0; i < header->event_num; i++){
            List_Length_Value* instance = (List_Length_Value*)malloc(sizeof(List_Length_Value));
            struct_length = parse_Length_Value(binary, &(instance->value));
            binary = binary + struct_length;
            length = length + struct_length;
            current->next = instance;
            current = current->next;
        }
    }

    struct_length = parse_u_int16_t(binary, &(header->reference_num));
    binary = binary + struct_length;
    length = length + struct_length;

    if(header->reference_num > 0){
        List_Length_Value* current = header->references;
        for(int i = 0; i < header->reference_num; i++){
            List_Length_Value* instance = (List_Length_Value*)malloc(sizeof(List_Length_Value));
            struct_length = parse_Length_Value(binary, &(instance->value));
            binary = binary + struct_length;
            length = length + struct_length;
            current->next = instance;
            current = current->next;
        }
    }

    struct_length = parse_u_int16_t(binary, &(header->cross_ref_num));
    binary = binary + struct_length;
    length = length + struct_length;

    if(header->cross_ref_num > 0){
        List_Length_Value* current = header->cross_refs;
        for(int i = 0; i < header->cross_ref_num; i++){
            List_Length_Value* instance = (List_Length_Value*)malloc(sizeof(List_Length_Value));
            struct_length = parse_Length_Value(binary, &(instance->value));
            binary = binary + struct_length;
            length = length + struct_length;
            current->next = instance;
            current = current->next;
        }
    }

    struct_length = parse_u_int16_t(binary, &(header->signature_num));
    binary = binary + struct_length;
    length = length + struct_length;

    if(header->signature_num > 0){
        List_Length_Value* current = header->signatures;
        for(int i = 0; i < header->signature_num; i++){
            List_Length_Value* instance = (List_Length_Value*)malloc(sizeof(List_Length_Value));
            struct_length = parse_Length_Value(binary, &(instance->value));
            binary = binary + struct_length;
            length = length + struct_length;
            current->next = instance;
            current = current->next;
        }
    }

    return length;
}

u_int32_t parse_list_Transaction(u_int8_t* binary, List_Transaction* header){
    u_int32_t length = 0;
    u_int32_t struct_length = 0;

    struct_length = parse_u_int32_t(binary, &(header->value.version));
    binary = binary + struct_length;
    length = length + struct_length;

    struct_length = parse_u_int64_t(binary, &(header->value.timestamp));
    binary = binary + struct_length;
    length = length + struct_length;

    struct_length = parse_u_int16_t(binary, &(header->value.event_num));
    binary = binary + struct_length;
    length = length + struct_length;

    if(header->value.event_num > 0){
        List_Length_Value* current = header->value.events;
        for(int i = 0; i < header->value.event_num; i++){
            List_Length_Value* instance = (List_Length_Value*)malloc(sizeof(List_Length_Value));
            struct_length = parse_Length_Value(binary, &(instance->value));
            binary = binary + struct_length;
            length = length + struct_length;
            current->next = instance;
            current = current->next;
        }
    }

    struct_length = parse_u_int16_t(binary, &(header->value.reference_num));
    binary = binary + struct_length;
    length = length + struct_length;

    if(header->value.reference_num > 0){
        List_Length_Value* current = header->value.references;
        for(int i = 0; i < header->value.reference_num; i++){
            List_Length_Value* instance = (List_Length_Value*)malloc(sizeof(List_Length_Value));
            struct_length = parse_Length_Value(binary, &(instance->value));
            binary = binary + struct_length;
            length = length + struct_length;
            current->next = instance;
            current = current->next;
        }
    }

    struct_length = parse_u_int16_t(binary, &(header->value.cross_ref_num));
    binary = binary + struct_length;
    length = length + struct_length;

    if(header->value.cross_ref_num > 0){
        List_Length_Value* current = header->value.cross_refs;
        for(int i = 0; i < header->value.cross_ref_num; i++){
            List_Length_Value* instance = (List_Length_Value*)malloc(sizeof(List_Length_Value));
            struct_length = parse_Length_Value(binary, &(instance->value));
            binary = binary + struct_length;
            length = length + struct_length;
            current->next = instance;
            current = current->next;
        }
    }

    struct_length = parse_u_int16_t(binary, &(header->value.signature_num));
    binary = binary + struct_length;
    length = length + struct_length;

    if(header->value.signature_num > 0){
        List_Length_Value* current = header->value.signatures;
        for(int i = 0; i < header->value.signature_num; i++){
            List_Length_Value* instance = (List_Length_Value*)malloc(sizeof(List_Length_Value));
            struct_length = parse_Length_Value(binary, &(instance->value));
            binary = binary + struct_length;
            length = length + struct_length;
            current->next = instance;
            current = current->next;
        }
    }

    return length;
}

void add_to_events_list_of_Transaction(Transaction* head, int length, void* value){
    List_Length_Value * current = head->events;
    if(head->event_num == 0){
        head->event_num= head->event_num + 1;
        List_Length_Value * v = (List_Length_Value * )malloc(sizeof(List_Length_Value));
        v->value.len = length;
        v->value.value = (void * )malloc(length);
        memcpy(v->value.value, value, length);
        current->next = v;
        return;
    }
    for (int i = 0;i < head->event_num;i++){
        current = current->next;
        if (head->event_num - 1 == i){
            head->event_num= head->event_num + 1;
            List_Length_Value * v = (List_Length_Value * )malloc(sizeof(List_Length_Value));
            v->value.len = length;
            v->value.value = (void * )malloc(length);
            memcpy(v->value.value, value, length);
            current->next = v;
            return;
        }
    }
}

void add_to_references_list_of_Transaction(Transaction* head, int length, void* value){
    List_Length_Value * current = head->references;
    if(head->reference_num == 0){
        head->reference_num= head->reference_num + 1;
        List_Length_Value * v = (List_Length_Value * )malloc(sizeof(List_Length_Value));
        v->value.len = length;
        v->value.value = (void * )malloc(length);
        memcpy(v->value.value, value, length);
        current->next = v;
        return;
    }
    for (int i = 0;i < head->reference_num;i++){
        current = current->next;
        if (head->reference_num - 1 == i){
            head->reference_num= head->reference_num + 1;
            List_Length_Value * v = (List_Length_Value * )malloc(sizeof(List_Length_Value));
            v->value.len = length;
            v->value.value = (void * )malloc(length);
            memcpy(v->value.value, value, length);
            current->next = v;
            return;
        }
    }
}

void add_to_cross_refs_list_of_Transaction(Transaction* head, int length, void* value){
    List_Length_Value * current = head->cross_refs;
    if(head->cross_ref_num == 0){
        head->cross_ref_num= head->cross_ref_num + 1;
        List_Length_Value * v = (List_Length_Value * )malloc(sizeof(List_Length_Value));
        v->value.len = length;
        v->value.value = (void * )malloc(length);
        memcpy(v->value.value, value, length);
        current->next = v;
        return;
    }
    for (int i = 0;i < head->cross_ref_num;i++){
        current = current->next;
        if (head->cross_ref_num - 1 == i){
            head->cross_ref_num= head->cross_ref_num + 1;
            List_Length_Value * v = (List_Length_Value * )malloc(sizeof(List_Length_Value));
            v->value.len = length;
            v->value.value = (void * )malloc(length);
            memcpy(v->value.value, value, length);
            current->next = v;
            return;
        }
    }
}

void add_to_signatures_list_of_Transaction(Transaction* head, int length, void* value){
    List_Length_Value * current = head->signatures;
    if(head->signature_num == 0){
        head->signature_num= head->signature_num + 1;
        List_Length_Value * v = (List_Length_Value * )malloc(sizeof(List_Length_Value));
        v->value.len = length;
        v->value.value = (void * )malloc(length);
        memcpy(v->value.value, value, length);
        current->next = v;
        return;
    }
    for (int i = 0;i < head->signature_num;i++){
        current = current->next;
        if (head->signature_num - 1 == i){
            head->signature_num= head->signature_num + 1;
            List_Length_Value * v = (List_Length_Value * )malloc(sizeof(List_Length_Value));
            v->value.len = length;
            v->value.value = (void * )malloc(length);
            memcpy(v->value.value, value, length);
            current->next = v;
            return;
        }
    }
}

void print_Transaction(Transaction* header){
    printf("version %d \n",header->version);
    printf("timestamp %llu \n",header->timestamp);
    printf("event_num %d \n",header->event_num);
    print_Length_Value((header->events));
    printf("reference_num %d \n",header->reference_num);
    print_Length_Value((header->references));
    printf("cross_ref_num %d \n",header->cross_ref_num);
    print_Length_Value((header->cross_refs));
    printf("signature_num %d \n",header->signature_num);
    print_Length_Value((header->signatures));
}

void free_events_of_Transaction(Transaction * header){
    if(header->events == NULL){
        return;
    }
    if (header->event_num > 0){
        List_Length_Value* current = header->events->next;
        List_Length_Value* next;
        for(int i = 0; i < header->event_num; i++){
            next = current->next;
            free_list_Length_Value(current);
            current = next;
        }
    }
}

void free_references_of_Transaction(Transaction * header){
    if(header->references == NULL){
        return;
    }
    if (header->reference_num > 0){
        List_Length_Value* current = header->references->next;
        List_Length_Value* next;
        for(int i = 0; i < header->reference_num; i++){
            next = current->next;
            free_list_Length_Value(current);
            current = next;
        }
    }
}

void free_cross_refs_of_Transaction(Transaction * header){
    if(header->cross_refs == NULL){
        return;
    }
    if (header->cross_ref_num > 0){
        List_Length_Value* current = header->cross_refs->next;
        List_Length_Value* next;
        for(int i = 0; i < header->cross_ref_num; i++){
            next = current->next;
            free_list_Length_Value(current);
            current = next;
        }
    }
}

void free_signatures_of_Transaction(Transaction * header){
    if(header->signatures == NULL){
        return;
    }
    if (header->signature_num > 0){
        List_Length_Value* current = header->signatures->next;
        List_Length_Value* next;
        for(int i = 0; i < header->signature_num; i++){
            next = current->next;
            free_list_Length_Value(current);
            current = next;
        }
    }
}

void free_list_Transaction(List_Transaction * header){
    if(header == NULL){
        return;
    }
    //It does not have to free (header->next).
    //(header->next) is define by python code, so (header->next->next) is managed by c 
    free_events_of_Transaction(header);
    free_references_of_Transaction(header);
    free_cross_refs_of_Transaction(header);
    free_signatures_of_Transaction(header);
    free(header);
}

void free_Transaction(Transaction * header){
    if(header == NULL){
        return;
    }
    free_events_of_Transaction(header);
    free_references_of_Transaction(header);
    free_cross_refs_of_Transaction(header);
    free_signatures_of_Transaction(header);
}

